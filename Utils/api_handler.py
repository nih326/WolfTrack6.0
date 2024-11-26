import requests
import json
import os
from dotenv import load_dotenv


def evaluate_job_match(job_title, job_description, resume_content):
    load_dotenv()
    OPENROUTER_API_KEY = os.getenv("API_KEY")
    
    prompt = f"""Please evaluate this job application and provide detailed feedback:

    Job Title: {job_title}

    Job Description:
    {job_description}

    Resume Content:
    {resume_content}

    Please analyze:
    1. Overall match score (0-100)
    2. Key matching skills and qualifications
    3. Missing or gaps in qualifications
    4. Specific suggestions for improvement
    """

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
            data=json.dumps({
                "model": "mistralai/mistral-7b-instruct:free",
                "messages": [
                    {"role": "system", "content": "You are an expert HR recruiter who provides detailed resume evaluations."},
                    {"role": "user", "content": prompt}
                ]
            })
        )
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    except Exception as e:
        return f"Error processing API response: {e}"
