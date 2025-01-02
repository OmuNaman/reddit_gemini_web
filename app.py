# app.py

from flask import Flask, render_template, request, Response, redirect, url_for, flash, jsonify
import os
import threading
import uuid
from dotenv import load_dotenv

from reddit_scraper import scrape_reddit_user
from gemini_processor import process_content

from extensions import db, login_manager, bcrypt, migrate
from models import User
from forms import RegistrationForm, LoginForm

from flask_login import login_user, current_user, logout_user, login_required

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or 'default_secret_key'  # Replace with a strong secret key

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') or 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions with the app
db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)

# Configure LoginManager
login_manager.login_view = 'login'  # Redirect to 'login' when login is required
login_manager.login_message_category = 'info'

# Global dictionary to track tasks
tasks = {}

def background_task(username, task_id):
    """
    Background task to scrape Reddit data and process it through Gemini API.
    Updates the tasks dictionary with progress.
    """
    try:
        tasks[task_id]['progress'] = 'Scraping Reddit data...'
        scraped_data = scrape_reddit_user(username, task_id, tasks)
        if not scraped_data:
            tasks[task_id]['progress'] = 'Failed to scrape Reddit data.'
            tasks[task_id]['status'] = 'Failed'
            return

        tasks[task_id]['progress'] = 'Processing data through Gemini API...'
        structured_report_path = process_content(username, scraped_data, task_id, tasks)
        if not structured_report_path or not os.path.exists(structured_report_path):
            tasks[task_id]['progress'] = 'Failed to process data with Gemini API.'
            tasks[task_id]['status'] = 'Failed'
            return

        tasks[task_id]['progress'] = 'Report generated successfully.'
        tasks[task_id]['status'] = 'Completed'
        tasks[task_id]['report_path'] = structured_report_path

    except Exception as e:
        print(f"Error in background task: {e}")
        tasks[task_id]['progress'] = 'An unexpected error occurred.'
        tasks[task_id]['status'] = 'Failed'

def get_unique_task_id():
    return uuid.uuid4().hex

@app.route('/', methods=['GET', 'POST'])
@login_required  # Require login for the main page
def index():
    if request.method == 'POST':
        reddit_username = request.form.get('reddit_username', '').strip()
        if not reddit_username:
            flash('Please enter a Reddit username.', 'danger')
            return redirect(url_for('index'))

        # Generate a unique task ID
        task_id = get_unique_task_id()
        tasks[task_id] = {
            'progress': 'Task started.',
            'status': 'In Progress',
            'report_path': None,
            'total_posts': 0,
            'scraped_posts': 0,
            'total_comments': 0,
            'scraped_comments': 0
        }

        # Start background thread
        thread = threading.Thread(target=background_task, args=(reddit_username, task_id))
        thread.start()

        flash('Your request is being processed. Please wait...', 'info')
        return redirect(url_for('progress_page', task_id=task_id))

    return render_template('index.html')

@app.route('/progress/<task_id>', methods=['GET'])
@login_required
def progress_page(task_id):
    """
    Render the progress page with a progress bar.
    """
    if task_id not in tasks:
        flash('Invalid task ID.', 'danger')
        return redirect(url_for('index'))
    return render_template('progress.html', task_id=task_id)

@app.route('/status/<task_id>', methods=['GET'])
@login_required
def status(task_id):
    """
    Endpoint to get the current status of the task.
    """
    if task_id not in tasks:
        return jsonify({'status': 'Invalid task ID.'}), 404

    task = tasks[task_id]
    total_posts = task.get('total_posts', 0)
    scraped_posts = task.get('scraped_posts', 0)
    total_comments = task.get('total_comments', 0)
    scraped_comments = task.get('scraped_comments', 0)

    return jsonify({
        'status': task.get('status', 'Unknown'),
        'progress': task.get('progress', ''),
        'total_posts': total_posts,
        'scraped_posts': scraped_posts,
        'total_comments': total_comments,
        'scraped_comments': scraped_comments
    })

@app.route('/download/<task_id>', methods=['GET'])
@login_required
def download(task_id):
    """
    Endpoint to download the generated report.
    """
    if task_id not in tasks:
        flash('Invalid task ID.', 'danger')
        return redirect(url_for('index'))
    if tasks[task_id]['status'] != 'Completed':
        flash('Report is not ready yet.', 'warning')
        return redirect(url_for('progress_page', task_id=task_id))

    report_path = tasks[task_id]['report_path']
    if not report_path or not os.path.exists(report_path):
        flash('Report file not found.', 'danger')
        return redirect(url_for('index'))

    # Define a generator to stream the file and delete it after sending
    def generate():
        with open(report_path, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                yield chunk
        # Delete the file after streaming
        os.remove(report_path)
        # Remove the task from the dictionary
        del tasks[task_id]

    return Response(generate(), mimetype='text/markdown', headers={
        'Content-Disposition': f'attachment; filename="{os.path.basename(report_path)}"'
    })

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Logged in successfully!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
