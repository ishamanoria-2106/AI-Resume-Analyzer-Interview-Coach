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

from utils.embeddings import EmbeddingEngine


def test_embedding_similarity():

    engine = EmbeddingEngine()

    resume = """
    Python
    Machine Learning
    SQL
    Pandas
    TensorFlow
    """

    job_description = """
    Looking for a Machine Learning Engineer
    with Python, SQL, TensorFlow and Pandas.
    """

    similarity = engine.calculate_similarity(
        resume,
        job_description
    )

    assert similarity is not None
    assert isinstance(similarity, float)
    assert 0 <= similarity <= 100