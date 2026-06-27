import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from PDF
    """
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


def clean_text(text: str) -> str:
    """
    Clean extracted text
    """
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = re.sub(r'[^\w\s.,@\-+/]', '', text)  # remove special chars
    return text.strip()


def parse_resume(pdf_path: str) -> dict:
    """
    Full pipeline: PDF → text → cleaned text
    """
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)

    return {
        "raw_text": raw_text,
        "cleaned_text": cleaned_text
    }