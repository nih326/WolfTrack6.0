import unittest
from app import extract_skills  # Ensure this import is correct

class TestSkillExtractor(unittest.TestCase):

    def test_extract_skills(self):
        job_description = "We are looking for a Python developer with experience in AWS and Docker."
        expected_skills = ['Python', 'AWS', 'Docker']
        found_skills = extract_skills(job_description)
        self.assertEqual(found_skills, expected_skills)

    def test_no_skills_found(self):
        job_description = "This job requires good communication skills."
        expected_skills = []
        found_skills = extract_skills(job_description)
        self.assertEqual(found_skills, expected_skills)

    def test_multiple_skills(self):
        job_description = "Looking for a JavaScript and Python developer."
        expected_skills = ['JavaScript', 'Python']
        found_skills = extract_skills(job_description)
        self.assertCountEqual(found_skills, expected_skills)

    def test_exact_match(self):
        job_description = "We are looking for a SQL expert."
        expected_skills = ['SQL']
        found_skills = extract_skills(job_description)
        self.assertEqual(found_skills, expected_skills)
        
    def test_list_format(self):
        job_description = """
        The following skills are required:
        - Python
        - Java
        - AWS
        """
        expected_skills = ['Python', 'AWS', 'Java']
        found_skills = extract_skills(job_description)
        self.assertEqual(sorted(found_skills), sorted(expected_skills))  # Sort both lists before comparison


    def test_empty_description(self):
        job_description = ""
        expected_skills = []
        found_skills = extract_skills(job_description)
        self.assertEqual(found_skills, expected_skills)

if __name__ == '__main__':
    unittest.main()
