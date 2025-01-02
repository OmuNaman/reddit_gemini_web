
# Reddit Gemini Analyzer

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Flask Version](https://img.shields.io/badge/flask-2.0%2B-blue.svg)

## [Live Demo](https://reddit-gemini-web.onrender.com/)

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Navigate to the Project Directory](#2-navigate-to-the-project-directory)
  - [3. Set Up a Virtual Environment](#3-set-up-a-virtual-environment)
  - [4. Activate the Virtual Environment](#4-activate-the-virtual-environment)
  - [5. Install Dependencies](#5-install-dependencies)
  - [6. Configure Environment Variables](#6-configure-environment-variables)
- [Running the Application Locally](#running-the-application-locally)
  - [1. Initialize Database Migrations](#1-initialize-database-migrations)
  - [2. Start the Flask Application](#2-start-the-flask-application)
  - [3. Access the Application](#3-access-the-application)
- [Usage](#usage)
- [Security Considerations](#security-considerations)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Getting Help](#getting-help)

---

## Introduction

**Reddit Gemini Analyzer** is a robust Flask-based web application designed to analyze Reddit user data. This tool scrapes publicly available Reddit data, processes it using the Gemini API, and generates insightful analysis reports. Whether you're aiming to understand user behavior, personality traits, or social dynamics, this tool provides detailed insights based on publicly available Reddit data.

---

## Features

- **Reddit Data Scraping:** Efficiently fetches posts and comments from any specified Reddit user.
- **Gemini API Integration:** Processes the scraped data to generate detailed and objective analysis reports.
- **Real-Time Progress Updates:** Provides users with live feedback on the scraping and processing stages.
- **Secure File Handling:** Ensures unique filenames to prevent conflicts and automatic cleanup of temporary files.
- **User Authentication:** Secure registration and login system to manage user access.
- **User-Friendly Interface:** Intuitive design for easy navigation and usage.

---

## Technologies Used

- **Backend:**
  - [Flask](https://flask.palletsprojects.com/) - Web framework for Python.
  - [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/) - Interact with Reddit's API.
  - [Google Generative AI](https://cloud.google.com/generative-ai/docs) - For processing and generating reports.
  - [Gunicorn](https://gunicorn.org/) - WSGI HTTP server for Python.
  - [Python Dotenv](https://saurabh-kumar.com/python-dotenv/) - Manage environment variables.
  - [Flask-Login](https://flask-login.readthedocs.io/) - User session management.
  - [Flask-WTF](https://flask-wtf.readthedocs.io/) - Form handling.
  - [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/) - Password hashing.
  - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - Database ORM.
  - [Flask-Migrate](https://flask-migrate.readthedocs.io/) - Database migrations.

- **Frontend:**
  - [Bootstrap 5](https://getbootstrap.com/) - For responsive and modern UI design.

- **Deployment:**
  - [Render](https://render.com/) - Cloud platform for deploying web applications.

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System:** Windows 10 or later, or any Linux distribution.
- **Python:** Version 3.8 or higher installed. [Download Python](https://www.python.org/downloads/)
- **Git:** Installed for version control. [Download Git](https://git-scm.com/downloads)

---

## Installation

Follow these steps to set up the project locally on your machine.

### 1. Clone the Repository

Cloning the repository means downloading a copy of the project to your local machine.

1. **Open Git Bash or Command Prompt:**
   - On Windows, you can use Git Bash or Command Prompt.
   - On macOS or Linux, use the Terminal.

2. **Run the Clone Command:**

   ```bash
   git clone https://github.com/OmuNaman-reddit_gemini_web.git
   ```

   > **Note:** Replace `https://github.com/OmuNaman-reddit_gemini_web.git` with the actual URL of your repository if different.

### 2. Navigate to the Project Directory

Change your current directory to the project folder to start working with the project files.

```bash
cd OmuNaman-reddit_gemini_web
```

### 3. Set Up a Virtual Environment

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python environments for them.

1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

   - This command creates a folder named `venv` in your project directory.

### 4. Activate the Virtual Environment

Activating the virtual environment ensures that the dependencies you install are confined to this project.

- **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **On macOS and Linux:**

  ```bash
  source venv/bin/activate
  ```

  > **Confirmation:** After activation, your command prompt should display `(venv)` indicating that the virtual environment is active.

### 5. Install Dependencies

Install all the required Python packages listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

- **Explanation:**
  - `pip` is the package installer for Python.
  - `-r requirements.txt` tells `pip` to install all the packages listed in the `requirements.txt` file.

### 6. Configure Environment Variables

Environment variables are used to store sensitive information like API keys and database URLs securely.

1. **Create a `.env` File:**

   - In the root directory of the project (`OmuNaman-reddit_gemini_web/`), create a file named `.env`.

2. **Add Your Environment Variables:**

   Open the `.env` file with a text editor (like Notepad, VS Code, or Sublime Text) and add the following lines:

   ```plaintext
   # .env

   REDDIT_CLIENT_ID=jqo7Fs3ovAYGi7o3mlbN0Q
   REDDIT_CLIENT_SECRET=9PGZV9RBlgyfsLTFa36s7SlCFwEGGA
   REDDIT_USER_AGENT=reddit-scraper
   GEMINI_API_KEY=AIzaSyAbkjWfB04trACavrWzANhGEWQhZOpGnpc
   GEMINI_API_ENDPOINT=https://api.gemini.example.com/v1/process  # Replace with actual endpoint
   SECRET_KEY=your_flask_secret_key  # Replace with a strong secret key
   DATABASE_URL=sqlite:///site.db  # Optional: Replace with your database URI if using PostgreSQL
   ```

   > **Important:** Replace the placeholder values (`your_flask_secret_key`, `https://api.gemini.example.com/v1/process`, etc.) with your actual credentials and endpoints.

3. **Update `.gitignore` to Exclude `.env`:**

   Ensure that the `.env` file is not tracked by Git to prevent sensitive information from being exposed.

   - Open or create a `.gitignore` file in the project root directory.
   - Add the following lines:

     ```gitignore
     # .gitignore

     venv/
     __pycache__/
     *.pyc
     .env
     ```

   > **Explanation:**
   > - `venv/` excludes the virtual environment folder.
   > - `__pycache__/` and `*.pyc` exclude compiled Python files.
   > - `.env` ensures that environment variables are kept secure.

---

## Running the Application Locally

After completing the installation steps, you can run the application locally to ensure everything works as expected.

### 1. Initialize Database Migrations

Database migrations help manage changes to your database schema over time.

1. **Ensure the Virtual Environment is Activated:**

   ```bash
   # On Windows
   venv\Scripts\activate

   # On macOS and Linux
   source venv/bin/activate
   ```

2. **Set the FLASK_APP Environment Variable:**

   This tells Flask which application to run.

   - **On Windows (Command Prompt):**

     ```bash
     set FLASK_APP=app.py
     ```

   - **On Windows (PowerShell):**

     ```powershell
     $env:FLASK_APP = "app.py"
     ```

   - **On macOS and Linux:**

     ```bash
     export FLASK_APP=app.py
     ```

3. **Initialize Migrations:**

   ```bash
   flask db init
   ```

   - **Explanation:** This command creates a `migrations` directory in your project, which will store all migration scripts.

4. **Create a Migration Script:**

   ```bash
   flask db migrate -m "Initial migration with User model"
   ```

   - **Explanation:** This command generates a migration script based on the changes detected in your models.

5. **Apply the Migration:**

   ```bash
   flask db upgrade
   ```

   - **Explanation:** This command applies the migration to your database, creating the necessary tables (like the `User` table).

### 2. Start the Flask Application

Run the Flask development server to start the application.

```bash
python app.py
```

- **Expected Output:**

  ```plaintext
   * Serving Flask app 'app'
   * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment.
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

### 3. Access the Application

1. **Open Your Web Browser:**

   - Launch your preferred web browser (e.g., Chrome, Firefox, Edge).

2. **Navigate to the Application:**

   - Enter the following URL in the address bar:

     ```
     http://127.0.0.1:5000/
     ```

   - **Result:** You should see the **Reddit Gemini Analyzer** homepage.

---

## Usage

Once the application is running locally, here's how you can use it:

1. **Register a New Account:**

   - Click on the **"Sign Up"** link in the navigation bar.
   - Fill out the registration form with a unique username, a valid email address, and a secure password.
   - Submit the form to create your account.
   - **Note:** After successful registration, you will be redirected to the login page.

2. **Login to Your Account:**

   - Click on the **"Login"** link in the navigation bar.
   - Enter your registered email and password.
   - Optionally, select **"Remember Me"** to stay logged in across sessions.
   - Submit the form to log in.
   - **Note:** Upon successful login, you will be redirected to the main page.

3. **Analyze a Reddit User:**

   - On the main page, you will see a form to enter a Reddit username.
   - Input the Reddit username you wish to analyze and click on the **"Generate Report"** button.
   - **Example:** Enter `exampleuser` and submit.

4. **Monitor Progress:**

   - After submitting, you'll be redirected to a progress page.
   - This page displays a real-time progress bar and statistics about the scraping and processing stages.
   - **Progress Indicators:**
     - **Total Posts:** Total number of posts by the user.
     - **Scraped Posts:** Number of posts successfully scraped.
     - **Total Comments:** Total number of comments by the user.
     - **Scraped Comments:** Number of comments successfully scraped.

5. **Download the Report:**

   - Once the processing is complete, a Markdown report will automatically be available for download.
   - The report contains a detailed analysis based on the user's Reddit activity.
   - Click the **"Download Report"** button to save the report to your device.

6. **Logout:**

   - Click on the **"Logout"** link in the navigation bar to end your session securely.

---

## Security Considerations

Ensuring the security of your application and user data is paramount. Here are some important considerations:

- **Environment Variables:**
  - Always use environment variables to store sensitive information like API keys and secrets.
  - Never expose your `.env` file or sensitive credentials in your code repository.

- **Password Hashing:**
  - User passwords are securely hashed using **Flask-Bcrypt** before being stored in the database.
  - This ensures that even if the database is compromised, plaintext passwords remain secure.

- **User Authentication:**
  - The application uses **Flask-Login** to manage user sessions securely.
  - Only authenticated users can access the main functionality of the application.

- **Input Validation:**
  - Forms are handled using **Flask-WTF**, which provides built-in validation to prevent malicious input.

- **Error Handling:**
  - The application includes error handling to manage unexpected issues during scraping and processing.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [PRAW Documentation](https://praw.readthedocs.io/)
- [Google Generative AI](https://cloud.google.com/generative-ai/docs)
- [Bootstrap 5](https://getbootstrap.com/)
- [Render](https://render.com/)
- [VS Code](https://code.visualstudio.com/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)
- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)
- [Flask-Bcrypt Documentation](https://flask-bcrypt.readthedocs.io/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Migrate Documentation](https://flask-migrate.readthedocs.io/)

---

## Getting Help

If you encounter any issues or have questions about setting up or using the **Reddit Gemini Analyzer**, feel free to reach out:

1. **Open an Issue:**
   - Navigate to the repository on GitHub.
   - Click on the **"Issues"** tab.
   - Click **"New Issue"** and provide a detailed description of your problem.

2. **Contact the Maintainer:**
   - If you have specific questions or need direct assistance, you can contact the project maintainer at [your-email@example.com](mailto:your-email@example.com).

3. **Community Forums:**
   - Join forums or communities related to Flask, Python, or web development for broader support.

---

**Thank you for using Reddit Gemini Analyzer!** ❤️❤️
