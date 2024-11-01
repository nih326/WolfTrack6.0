import unittest
from flask import Flask
from app import app
import json
import os

print("Current working directory:", os.getcwd())



class TestInterviewPrep(unittest.TestCase):

    def setUp(self):
        # Use the actual app from app.py to keep routes and templates intact
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.resource_json_path = os.path.join(os.path.dirname(__file__), '../data/resource.json')
        self.valid_pdf_path = os.path.join(os.path.dirname(__file__), '../docs/WolfTrack_4.0_UseCase.pdf')


    def test_interview_prep_page_loads(self):
        # Test that the Interview Preparation Resources page loads successfully
        response = self.client.get('/interview-prep')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Interview Preparation Resources', response.data)

    def test_resources_displayed(self):
        # Load mock data from resource.json to verify resources appear on the page
        with open(self.resource_json_path) as f:
            resources = json.load(f)
        
        response = self.client.get('/interview-prep')
        for resource in resources:
            # Check if each resource title is in the response data
            self.assertIn(resource['title'].encode(), response.data)

    def test_download_pdf_valid_id(self):
        # Test downloading a PDF with a valid resource ID
        with open(self.resource_json_path) as f:
            resources = json.load(f)
        
        valid_resource = next((res for res in resources if 'pdf' in res), None)
        if valid_resource:
            response = self.client.get(f'/download/{valid_resource["id"]}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/pdf')
        else:
            self.skipTest("No resource with a PDF found in test data.")

    def test_download_pdf_invalid_id(self):
        # Test downloading a PDF with an invalid resource ID
        response = self.client.get('/download/9999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'File not found', response.data)

    def test_required_title(self):
        # Verify that each resource has a title displayed on the page
        response = self.client.get('/interview-prep')

if __name__ == '__main__':
    unittest.main()