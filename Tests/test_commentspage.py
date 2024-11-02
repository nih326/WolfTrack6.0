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

    def test_leave_review_html_structure(self):
        response = self.client.get('/student/leave_review')
        self.assertIn(b'<form id="commentForm">', response.data)
        self.assertIn(b'<input type="text" id="nameInput"', response.data)
        self.assertIn(b'<textarea id="commentInput"', response.data)
        self.assertIn(b'<div class="stars" id="starRating">', response.data)
        self.assertIn(b'<button type="submit">Submit</button>', response.data)
        self.assertIn(b'<button id="clearComments">Clear All Comments</button>', response.data)

    def test_empty_name_field(self):
        response = self.client.post('/student/leave_review', data={'name': '', 'comment': 'Test comment', 'rating': 5})
        self.assertIn(b'Name is required', response.data)

    def test_empty_comment_field(self):
        response = self.client.post('/student/leave_review', data={'name': 'John', 'comment': '', 'rating': 5})
        self.assertIn(b'Comment is required', response.data)

    def test_empty_review_field(self):
        response = self.client.post('/student/leave_review', data={'name': 'John', 'comment': 'Test comment', 'rating': 0})
        self.assertIn(b'Rating is required', response.data)
