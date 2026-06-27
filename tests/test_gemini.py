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

from utils.gemini_client import GeminiClient


def test_gemini_client_initialization():
    """
    Test that GeminiClient initializes successfully.
    """
    client = GeminiClient()
    assert client is not None
    assert client.model is not None