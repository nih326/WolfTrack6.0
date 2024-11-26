from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        cleaned_text = text.replace('\n', ' ').strip()
        return cleaned_text
    except Exception as e:
        print(f"Error extracting PDF content: {e}")
        return None
