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

from utils.ats_score import ATSScorer


def test_ats_score():

    scorer = ATSScorer()

    resume = """
    Python
    SQL
    Machine Learning
    TensorFlow
    Bachelor's Degree
    3 years experience
    """

    job_description = """
    Looking for an AI Engineer with
    Python,
    SQL,
    Machine Learning,
    TensorFlow,
    Bachelor's Degree,
    3 years experience.
    """

    result = scorer.calculate_ats_score(
        resume,
        job_description
    )

    assert isinstance(result, dict)

    expected_keys = [
        "skill_score",
        "keyword_score",
        "experience_score",
        "education_score",
        "final_ats_score"
    ]

    for key in expected_keys:
        assert key in result

    assert 0 <= result["final_ats_score"] <= 100