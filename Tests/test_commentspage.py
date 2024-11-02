import unittest
from unittest.mock import patch
from app import app

class TestLeaveReview(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_leave_review_route(self):
        response = self.client.get('/student/leave_review')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>WolfTrack 6.0</h1>', response.data)
