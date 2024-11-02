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

    def test_case_insensitive(self):
        job_description = "We need a Java and C++ programmer."
        expected_skills = ['Java', 'C++']
        found_skills = extract_skills(job_description)
        self.assertEqual(found_skills, expected_skills)

if __name__ == '__main__':
    unittest.main()
