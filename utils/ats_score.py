import re


class ATSScorer:

    def __init__(self):
        pass

    # -------------------------
    # Extract skills
    # -------------------------
    def extract_skills(self, text):

        skills_database = [
            "python",
            "sql",
            "excel",
            "power bi",
            "tableau",
            "tensorflow",
            "pytorch",
            "scikit-learn",
            "machine learning",
            "nlp",
            "mongodb",
            "postgresql",
            "rest api",
            "docker",
            "aws",
            "git"
        ]

        text = text.lower()

        found_skills = []

        for skill in skills_database:
            if skill in text:
                found_skills.append(skill)

        return found_skills

    # -------------------------
    # Skill Match
    # -------------------------
    def calculate_skill_score(self, resume_text, jd_text):

        resume_skills = set(
            self.extract_skills(resume_text)
        )

        jd_skills = set(
            self.extract_skills(jd_text)
        )

        if len(jd_skills) == 0:
            return 0

        matched = resume_skills.intersection(
            jd_skills
        )

        return (
            len(matched)
            / len(jd_skills)
        ) * 100

    # -------------------------
    # Keyword Match
    # -------------------------
    def calculate_keyword_score(
        self,
        resume_text,
        jd_text
    ):

        resume_words = set(
            re.findall(
                r'\b\w+\b',
                resume_text.lower()
            )
        )

        jd_words = set(
            re.findall(
                r'\b\w+\b',
                jd_text.lower()
            )
        )

        if len(jd_words) == 0:
            return 0

        common_words = (
            resume_words.intersection(
                jd_words
            )
        )

        return (
            len(common_words)
            / len(jd_words)
        ) * 100

    # -------------------------
    # Experience Score
    # -------------------------
    def calculate_experience_score(
        self,
        resume_text
    ):

        experience_keywords = [
            "intern",
            "internship",
            "experience",
            "developer",
            "engineer",
            "analyst"
        ]

        score = 0

        for word in experience_keywords:
            if word in resume_text.lower():
                score += 15

        return min(score, 100)

    # -------------------------
    # Education Score
    # -------------------------
    def calculate_education_score(
        self,
        resume_text
    ):

        education_keywords = [
            "b.tech",
            "bachelor",
            "computer science",
            "information technology",
            "data science",
            "artificial intelligence"
        ]

        score = 0

        for word in education_keywords:
            if word in resume_text.lower():
                score += 20

        return min(score, 100)

    # -------------------------
    # Final ATS Score
    # -------------------------
    def calculate_ats_score(
        self,
        resume_text,
        jd_text
    ):

        skill_score = self.calculate_skill_score(
            resume_text,
            jd_text
        )

        keyword_score = self.calculate_keyword_score(
            resume_text,
            jd_text
        )

        experience_score = (
            self.calculate_experience_score(
                resume_text
            )
        )

        education_score = (
            self.calculate_education_score(
                resume_text
            )
        )

        final_score = (
            skill_score * 0.40
            + keyword_score * 0.30
            + experience_score * 0.20
            + education_score * 0.10
        )

        return {
            "skill_score": round(skill_score, 2),
            "keyword_score": round(keyword_score, 2),
            "experience_score": round(experience_score, 2),
            "education_score": round(education_score, 2),
            "final_ats_score": round(final_score, 2)
        }