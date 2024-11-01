import unittest
from flask import Flask
from app import app, LoginForm 
import os

# Load environment variables
#load_dotenv() 

class TestSignupFormValidation(unittest.TestCase):

    def setUp(self):
        # Use the actual app from app.py to keep routes and templates intact
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SECRET_KEY'] = 'thisisasecretkey'
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        self.client = self.app.test_client()
        self.test_username = os.getenv("TEST_USERNAME")
        self.test_password = os.getenv("TEST_PASSWORD")


    def test_wrong_user(self):
        # Testing password exceeding maximum length with a POST request
        response = self.client.post(
            '/login',
            data={
                "username": "qwer",
                "password": "diyadiya06#",
                "usertype": "student"
            }
        )

        # Check if the response contains the expected error message
        self.assertIn(b"User does not exist", response.data)

    def test_wrong_usertype(self):
        # Testing password exceeding maximum length with a POST request
        response = self.client.post(
            '/login',
            data={
                "username": "qwert",
                "password": "diyadiya06#",
                "usertype": "admin"
            }
        )

        # Check if the response contains the expected error message
        self.assertIn(b"Invalid credentials", response.data)

    def test_wrong_password(self):
        # Testing password exceeding maximum length with a POST request
        response = self.client.post(
            '/login',
            data={
                "username": "qwert",
                "password": "ya0dfgssgr#",
                "usertype": "student"
            }
        )

        # Check if the response contains the expected error message
        self.assertIn(b"Invalid credentials", response.data)

    def test_correct_user_redirects_to_student(self):
        # Testing a correct login that should redirect to the student page
        response = self.client.post(
            '/login',
            data={
            "username": "qwert",
            "password": "diyadiya06#",
            "usertype": "student"
            },
            follow_redirects=False  # Set to False to capture the redirect response
        )

        # Check if the response has a 302 status code for redirection
        self.assertEqual(response.status_code, 302)

        # Check that the redirection location is the student page
        self.assertIn('/student', response.headers['Location'])

    def test_required_username(self):
        # Testing password exceeding maximum length with a POST request
        response = self.client.post(
            '/login',
            data={
                "password": "diyadiya06#",
                "usertype": "student"
            }
        )

        # Check if the response contains the expected error message
        self.assertIn(b"This field is required.", response.data)

    def test_required_password(self):
        # Testing password exceeding maximum length with a POST request
        response = self.client.post(
            '/login',
            data={
                "username": "qwert",
                "usertype": "student"
            }
        )

        # Check if the response contains the expected error message
        self.assertIn(b"This field is required.", response.data)

if __name__ == '__main__':
    unittest.main()
