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

from utils.report_generator import generate_pdf_report


def test_report_generation():

    ats_result = {
        "skill_score": 85,
        "keyword_score": 80,
        "experience_score": 90,
        "education_score": 75,
        "final_ats_score": 83
    }

    ai_analysis = """
Strengths
• Strong Python skills
• Good Machine Learning knowledge

Weaknesses
• Limited AWS experience
"""

    interview_questions = """
1. Explain Machine Learning.
2. What is TensorFlow?
3. Difference between CNN and RNN?
"""

    roadmap = """
30 Days
• Learn Docker

60 Days
• Learn AWS

90 Days
• Build AI Projects
"""

    output_path = "test_report.pdf"

    pdf_file = generate_pdf_report(
        ats_result,
        ai_analysis,
        interview_questions,
        roadmap,
        output_path
    )

    assert os.path.exists(pdf_file)
    assert os.path.getsize(pdf_file) > 0

    # Clean up after test
    os.remove(pdf_file)