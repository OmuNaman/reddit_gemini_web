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
- [Usage](#usage)
- [Deployment](#deployment)
  - [Deploying with Render](#deploying-with-render)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Getting Help](#getting-help)

---

## Introduction

**Reddit Gemini Analyzer** is a robust Flask-based web application designed to scrape Reddit user data, process it through the Gemini API, and generate comprehensive, insightful analysis reports. Whether you're aiming to understand user behavior, personality traits, or social dynamics, this tool provides detailed insights based on publicly available Reddit data.

## Features

- **Reddit Data Scraping:** Efficiently fetches posts and comments from any specified Reddit user.
- **Gemini API Integration:** Processes the scraped data to generate detailed and objective analysis reports.
- **Real-Time Progress Updates:** Provides users with live feedback on the scraping and processing stages.
- **Secure File Handling:** Ensures unique filenames to prevent conflicts and automatic cleanup of temporary files.
- **User-Friendly Interface:** Intuitive design for easy navigation and usage.

## Technologies Used

- **Backend:**

  - [Flask](https://flask.palletsprojects.com/) - Web framework for Python.
  - [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/) - Interact with Reddit's API.
  - [Google Generative AI](https://cloud.google.com/generative-ai/docs) - For processing and generating reports.
  - [Gunicorn](https://gunicorn.org/) - WSGI HTTP server for Python.
  - [Python Dotenv](https://saurabh-kumar.com/python-dotenv/) - Manage environment variables.
- **Frontend:**

  - [Bootstrap 5](https://getbootstrap.com/) - For responsive and modern UI design.
- **Deployment:**

  - [Render](https://render.com/) - Cloud platform for deploying web applications.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System:** Windows 10 or later.
- **Python:** Version 3.8 or higher installed. [Download Python](https://www.python.org/downloads/)
- **Git:** Installed for version control. [Download Git](https://git-scm.com/downloads)
- **Render Account:** For deploying the application. [Sign Up on Render](https://render.com/)

## Installation

Follow these steps to set up the project locally on your Windows machine using VS Code.

### 1. Clone the Repository

First, clone the repository to your local machine using Git.

```bash
git clone https://github.com/OmuNaman/reddit_gemini.git
```

### 2. Navigate to the Project Directory

Change your current directory to the project folder.

```bash
cd reddit_gemini
```

### 3. Set Up a Virtual Environment

Creating a virtual environment isolates project dependencies and ensures that your project runs in a controlled environment.

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Activate the virtual environment to start using it.

```bash
venv\Scripts\activate
```

After activation, your command prompt should display `(venv)` indicating that the virtual environment is active.

### 5. Install Dependencies

Install all required Python packages using `pip`.

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Sensitive information like API keys should never be hard-coded. Instead, use environment variables to manage them securely.

1. **Create a `.env` File:**

   In the root directory of the project, create a file named `.env`.
2. **Add the Following Environment Variables:**

   ```plaintext
   # .env

   REDDIT_CLIENT_ID=jqo7Fs3ovAYGi7o3mlbN0Q
   REDDIT_CLIENT_SECRET=9PGZV9RBlgyfsLTFa36s7SlCFwEGGA
   REDDIT_USER_AGENT=reddit-scraper
   GEMINI_API_KEY=AIzaSyAbkjWfB04trACavrWzANhGEWQhZOpGnpc
   GEMINI_API_ENDPOINT=https://api.gemini.example.com/v1/process  # Replace with actual endpoint
   SECRET_KEY=your_flask_secret_key  # Replace with a strong secret key
   ```

   > **⚠️ Security Warning:** **Never commit your `.env` file** to version control. Ensure it’s included in your `.gitignore` file to prevent accidental exposure of sensitive data.
   >
3. **Update `.gitignore` to Exclude `.env`:**

   Create or update the `.gitignore` file in the project root with the following line:

   ```gitignore
   # .gitignore

   venv/
   __pycache__/
   *.pyc
   .env
   ```

## Running the Application Locally

After completing the installation steps, you can run the application locally to ensure everything works as expected.

1. **Ensure the Virtual Environment is Activated:**

   ```bash
   venv\Scripts\activate
   ```
2. **Start the Flask Application:**

   ```bash
   python app.py
   ```

   You should see output similar to:

   ```plaintext
    * Serving Flask app 'app'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment.
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```
3. **Access the Application:**

   Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/). You should see the **Reddit Gemini Analyzer** homepage.

## Usage

1. **Enter a Reddit Username:**

   On the homepage, input the Reddit username you wish to analyze and click on the "Generate Report" button.
2. **Monitor Progress:**

   You'll be redirected to a progress page that displays a real-time progress bar and statistics about the scraping and processing stages.
3. **Download the Report:**

   Once the processing is complete, a Markdown report will automatically download to your device. This report contains a detailed analysis based on the user's Reddit activity.

## Deployment

Your application is already deployed on [Render](https://render.com/) and can be accessed via [https://reddit-gemini-web.onrender.com/](https://reddit-gemini-web.onrender.com/). Here's a quick overview of the deployment setup:

### Deploying with Render

1. **Push Your Code to GitHub:**

   Ensure all your files, including `render.yaml`, are committed and pushed to your GitHub repository.

   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin master
   ```
2. **Connect Render to Your GitHub Repository:**

   - Log in to [Render](https://render.com/).
   - Click on "New" and select "Web Service".
   - Connect your GitHub account and select the `reddit_gemini` repository.
   - Render will automatically detect the `render.yaml` file and configure the service accordingly.
3. **Configure Environment Variables on Render:**

   Ensure all environment variables listed in `render.yaml` are correctly set in Render’s dashboard for your service.
4. **Deploy:**

   Render will build and deploy your application. Monitor the deployment logs for any issues.
5. **Access Your Live Application:**

   Once deployed, access your application at [https://reddit-gemini-web.onrender.com/](https://reddit-gemini-web.onrender.com/).

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create an issue or submit a pull request.

1. **Fork the Repository**
2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Commit Your Changes**

   ```bash
   git commit -m "Add some feature"
   ```
4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeatureName
   ```
5. **Open a Pull Request**

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [PRAW Documentation](https://praw.readthedocs.io/)
- [Google Generative AI](https://cloud.google.com/generative-ai/docs)
- [Bootstrap 5](https://getbootstrap.com/)
- [Render](https://render.com/)
- [VS Code](https://code.visualstudio.com/)

---

## Getting Help

If you encounter any issues or have questions, feel free to open an issue in the repository or reach out to me directly.

---

**Thank you for using Reddit Gemini Analyzer!** ❤️❤️
