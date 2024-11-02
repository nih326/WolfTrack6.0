import unittest
from unittest.mock import patch
from app import app

class TestNetworkingContacts(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_networking_contacts_route(self):
        response = self.client.get('/student/networking_contacts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Networking Contacts</h1>', response.data)
        
    def test_networking_contacts_html_structure(self):
        response = self.client.get('/student/networking_contacts')
        self.assertIn(b'<table id="contactsTable">', response.data)
        self.assertIn(b'<input type="text" id="name"', response.data)
        self.assertIn(b'<input type="text" id="company"', response.data)
        self.assertIn(b'<input type="text" id="role"', response.data)
        self.assertIn(b'<textarea id="notes"', response.data)
        self.assertIn(b'<button type="submit">Add Contact</button>', response.data)
