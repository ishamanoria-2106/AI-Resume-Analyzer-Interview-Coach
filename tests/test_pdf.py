import os
import sys

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from utils.pdf_parser import extract_text_from_pdf


def test_pdf_extraction():

    pdf_path = os.path.join(
        "sample_data",
        "resumes",
        "data_analyst_resume.pdf"
    )

    text = extract_text_from_pdf(pdf_path)

    assert text is not None
    assert isinstance(text, str)
    assert len(text) > 100