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
- [How to Get API Keys](#how-to-get-api-keys)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Getting Help](#getting-help)

---

## Introduction

**Reddit Gemini Analyzer** is a Flask-based web application designed to analyze Reddit user data. This tool scrapes publicly available Reddit data, processes it using a custom API, and generates insightful analysis reports. The goal is to provide users with a secure, customizable platform for exploring Reddit activity.

## Features

- **Reddit Data Scraping:** Fetches posts and comments for analysis.
- **API Integration:** Processes data to generate detailed analysis reports.
- **Real-Time Progress Updates:** Feedback during scraping and processing stages.
- **Secure Environment Setup:** Encourages users to use their own API keys and environment variables.
- **User-Friendly Interface:** Intuitive design for easy navigation and usage.

## Technologies Used

- **Backend:**
  - [Flask](https://flask.palletsprojects.com/) - Web framework for Python.
  - [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/) - Interact with Reddit's API.
  - [Gunicorn](https://gunicorn.org/) - WSGI HTTP server for Python.
  - [Python Dotenv](https://saurabh-kumar.com/python-dotenv/) - Manage environment variables.

- **Frontend:**
  - [Bootstrap 5](https://getbootstrap.com/) - For responsive UI design.

## Prerequisites

Before you begin, ensure you have the following:

- **Operating System:** Windows 10 or later, or any Linux distribution.
- **Python:** Version 3.8 or higher. [Download Python](https://www.python.org/downloads/)
- **Git:** Installed for version control. [Download Git](https://git-scm.com/downloads)

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine using Git.

```bash
git clone https://github.com/YourGitHub/reddit_gemini.git
```

### 2. Navigate to the Project Directory

Change your current directory to the project folder.

```bash
cd reddit_gemini
```

### 3. Set Up a Virtual Environment

Create a virtual environment to isolate project dependencies.

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Activate the virtual environment.

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 5. Install Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

For security, use your own API keys and credentials. Here’s how to set them up:

1. **Create a `.env` File:**

   In the root directory of the project, create a file named `.env`.

2. **Add Your Environment Variables:**

   ```plaintext
   # .env

   REDDIT_CLIENT_ID=<your_reddit_client_id>
   REDDIT_CLIENT_SECRET=<your_reddit_client_secret>
   REDDIT_USER_AGENT=<your_custom_user_agent>
   API_KEY=<your_api_key>
   API_ENDPOINT=<your_api_endpoint>
   SECRET_KEY=<your_flask_secret_key>
   ```

   > Replace placeholders (`<your_reddit_client_id>`, etc.) with your own credentials. You can generate these keys from respective service providers.

3. **Update `.gitignore`:**

   Ensure `.env` is included in `.gitignore` to prevent accidental exposure of sensitive data.

   ```gitignore
   # .gitignore

   venv/
   __pycache__/
   *.pyc
   .env
   ```

## Running the Application Locally

1. **Activate the Virtual Environment:**

   ```bash
   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

2. **Start the Flask Application:**

   ```bash
   python app.py
   ```

3. **Access the Application:**

   Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. **Enter Your Own API Details:**

   Use the `.env` file to securely store your API keys.

2. **Analyze a Reddit User:**

   Input a Reddit username and generate a report. The report will include a detailed analysis based on the user’s activity.

3. **Download Reports:**

   Once processing is complete, you can download the generated report directly from the interface.

## How to Get API Keys

### 1. Getting Reddit API Keys

   - Go to [Reddit's App Preferences](https://www.reddit.com/prefs/apps).
   - Scroll down and click on **Create App or Script**.
   - Fill in the fields:
     - **Name:** Choose a name for your app.
     - **App Type:** Select "script".
     - **Description:** Optional.
     - **Redirect URI:** Use `http://localhost:8000` or any URL (it’s not critical here).
     - **About URL:** Optional.
   - Save changes.
   - Copy your **client ID** and **client secret** from the app details.

### 2. Getting a Custom API Key

   - Visit the API provider’s website (e.g., Gemini API).
   - Sign up for an account if you don’t have one.
   - Go to the developer dashboard or API keys section.
   - Create a new key and give it a name.
   - Copy the key and paste it into the `.env` file under `API_KEY`.

### 3. Generating a Flask Secret Key

   - Open a terminal.
   - Run the following Python command to generate a secure key:
     ```python
     import os
     print(os.urandom(24))
     ```
   - Copy the output and paste it into the `.env` file under `SECRET_KEY`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [PRAW Documentation](https://praw.readthedocs.io/)
- [Bootstrap 5](https://getbootstrap.com/)
- [VS Code](https://code.visualstudio.com/)

## Getting Help

If you encounter issues, feel free to open an issue on the repository or contact the maintainer directly.

---

**Thank you for using Reddit Gemini Analyzer!**
