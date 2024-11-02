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
