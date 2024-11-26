import os
from flask import render_template, request
from Utils.resume_scraper import extract_text_from_pdf
from Utils.api_handler import evaluate_job_match

def analyze_resume():
    try:
        # Get form data
        job_title = request.form['job_title']
        job_description = request.form['job_description']
        
        # Ensure the 'uploads' directory exists
        upload_folder = "uploads"
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # Save and extract text from uploaded file
        resume_file = request.files['resume']
        resume_path = os.path.join(upload_folder, resume_file.filename)
        resume_file.save(resume_path)

        # Extract text from the uploaded PDF
        resume_content = extract_text_from_pdf(resume_path)
        if not resume_content:
            raise ValueError("Failed to extract content from the uploaded resume.")

        # Call API to evaluate the resume
        analysis_result = evaluate_job_match(job_title, job_description, resume_content)

        # Render the results in the frontend
        return render_template('analysis_result.html', result=analysis_result)

    except KeyError as e:
        print(f"Missing form field: {e}")
        return "Error: Missing form field. Please provide all required inputs.", 400
    except FileNotFoundError as e:
        print(f"File handling error: {e}")
        return "Error: Unable to process the uploaded file. Please try again.", 400
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Error: {e}", 500
