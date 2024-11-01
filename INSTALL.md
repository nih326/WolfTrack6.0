## Getting Started & Installation:

- ### Prerequisite:

  - Download [Python3.x](https://www.python.org/downloads/).

- ### Installation:

  E.g If you downloaded `Python 3.8.7` above, then

  **Steps to setup virtual environment**

  - Create a virtual environment:

    `python3.8 -m venv test_env`

  - Activate the virtual environment:

    `source test_env/bin/activate`

  - Build the virtual environment:(must be present in [project root directory](https://github.com/nih326/WolfTrack6.0))

    `pip install -r requirements.txt`

- ### Run Instructions

  **To run/test the site locally:**

  - Clone [WolfTrack github repo](https://github.com/nih326/WolfTrack6.0).

  - Navigate to [project directory](https://github.com/nih326/WolfTrack6.0).

  - Run `python main.py` or `python3 main.py` <br> <br>
    If there is a certificate error coming up for nltk stopwords download: <br>

    - search for "Install Certificates.command" in finder and open it. Its a script that will install required Certificates. <br>
    - Run the above command again.

  - Site will be hosted at:
    `http://127.0.0.1:5000/`

- ### API Setup
**Create an Account:**

  Go to the Adzuna Developer portal developer.adzuna.com.
  Sign up for an account to access the API. You might need to provide some basic details about your application, such as the name, purpose, and contact information.

**Get API Credentials:**

  Log in to your Adzuna Developer account.
  Find the section to create an API application.
  Create a new application to generate API credentials (usually API keys or tokens). These credentials are necessary to authenticate your requests to the Adzuna API.

**Change URL:**

  Update the adzuna_url in your app.py - using the newly obtained credentials. This updated URL should reflect the API endpoint along with your authentication credentials for accessing the Adzuna API.
