import unittest
from flask import Flask
from app import RegisterForm  # Import your actual SignupForm here
from flask_wtf import FlaskForm

class TestSignupFormValidation(unittest.TestCase):

    def setUp(self):
        # Create a test Flask app instance
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'thisisasecretkey'
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing

    def test_username_less_min_length(self):
        # Testing username at lesser than minimum length boundary
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "a", "password": "password123#", "confirm_password": "password123#", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("Field must be between 4 and 20 characters long.", form.username.errors)

    def test_username_max_length(self):
        # Testing username at maximum length boundary
        with self.app.test_request_context(method="POST", data={"name":"abc","username": "a" * 20, "password": "password123#", "confirm_password": "password123#", "usertype": "student"}):
            form = RegisterForm()
            self.assertTrue(form.validate())

    def test_username_min_length(self):
        # Testing username at minimum length boundary
        with self.app.test_request_context(method="POST", data={"name":"abc","username": "a" * 4, "password": "password123#", "confirm_password": "password123#", "usertype": "student"}):
            form = RegisterForm()
            self.assertTrue(form.validate())

    def test_username_exceeds_max_length(self):
        # Testing username exceeding maximum length
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "a" * 24, "password": "password123#", "confirm_password": "password123#", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("Field must be between 4 and 20 characters long.", form.username.errors)

    def test_password_min_length(self):
        # Testing password at minimum length boundary
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user123", "password": "pass1#", "confirm_password": "pass1#", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("Field must be between 8 and 20 characters long.", form.password.errors)


    def test_password_exceeds_max_length(self):
        # Testing password exceeding maximum length
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user123", "password": "p" * 21, "confirm_password": "p" * 21, "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("Field must be between 8 and 20 characters long.", form.password.errors)

    def test_password_correct_length(self):
        # Testing password of correct length
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user123", "password": "password12#", "confirm_password": "password12#", "usertype": "student"}):
            form = RegisterForm()
            self.assertTrue(form.validate())

    def test_confirm_password_mismatch(self):
        # Testing confirm_password mismatch
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user12345", "password": "password123#", "confirm_password": "differentpass1#", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("Passwords do not match", form.confirm_password.errors)

    def test_usertype_selection(self):
        # Testing with a valid usertype
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user1234", "password": "password123#", "confirm_password": "password123#", "usertype": "student"}):
            form = RegisterForm()
            self.assertTrue(form.validate())

    def test_password_just_numbers(self):
        # Testing with a password of just numbers
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user1234", "password": "12345678", "confirm_password": "12345678", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("Password should contain atleast one letter, number and special character", form.password.errors)

    def test_password_just_letters(self):    
        #Testing with a password of just letters
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user1234", "password": "abcdefgh", "confirm_password": "abcdefgh", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("Password should contain atleast one letter, number and special character", form.password.errors)

    def test_password_numbers_letters(self):    
        #Testing with a password of just letters
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user1234", "password": "abcdefgh123", "confirm_password": "abcdefgh123", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("Password should contain atleast one letter, number and special character", form.password.errors)
    
    def test_password_valid(self):    
        #Testing with a password of just letters
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user1234", "password": "abcdefgh12#", "confirm_password": "abcdefgh12#", "usertype": "student"}):
            form = RegisterForm()
            self.assertTrue(form.validate())

    def test_required_name(self):    
        #Testing with a password of just letters
        with self.app.test_request_context(method="POST", data={"username": "user1234", "password": "abcdefgh12#", "confirm_password": "abcdefgh12#", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("This field is required.", form.name.errors)

    def test_required_username(self):    
        #Testing with a password of just letters
        with self.app.test_request_context(method="POST", data={"name":"abc", "password": "abcdefgh12#", "confirm_password": "abcdefgh12#", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("This field is required.", form.username.errors)

    
    def test_required_password(self):    
        #Testing with a password of just letters
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user1234", "confirm_password": "abcdefgh12#", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("This field is required.", form.password.errors)

    def test_required_confirm_password(self):    
        #Testing with a password of just letters
        with self.app.test_request_context(method="POST", data={"name":"abc", "username": "user1234",  "password": "abcdefgh12#", "usertype": "student"}):
            form = RegisterForm()
            self.assertFalse(form.validate())
            self.assertIn("This field is required.", form.confirm_password.errors)

if __name__ == '__main__':
    unittest.main()
