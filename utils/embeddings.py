from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class EmbeddingEngine:
    def __init__(self):
        """
        Load embedding model once
        """
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_embedding(self, text):
            """
            Convert text into embedding vector.
            Normalize embeddings for better cosine similarity.
            """
            return self.model.encode(
                text,
                normalize_embeddings=True
            )

    def calculate_similarity(self, resume_text, jd_text):
        """
        Compare resume and job description
        """

        resume_embedding = self.create_embedding(resume_text)
        jd_embedding = self.create_embedding(jd_text)

        similarity = cosine_similarity(
            [resume_embedding],
            [jd_embedding]
        )[0][0]

        score = round(float(similarity) * 100, 2)
        return score