import os
from dotenv import load_dotenv
import google.generativeai as genai

from utils.prompts import (
    RESUME_ANALYSIS_PROMPT,
    INTERVIEW_QUESTIONS_PROMPT,
    ROADMAP_PROMPT
)

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiClient:

    def __init__(self):

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate_response(self, prompt):

        try:
            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            return f"Gemini API Error: {str(e)}"
        
    # -------------------------
    # Resume Analysis
    # -------------------------
    def analyze_resume(
        self,
        resume_text,
        job_description
    ):

        prompt = RESUME_ANALYSIS_PROMPT.format(
            resume=resume_text,
            job_description=job_description
        )

        return self.generate_response(prompt)
    
    # -------------------------
    # Interview Questions
    # -------------------------
    def generate_interview_questions(
        self,
        resume_text,
        job_description
    ):

        prompt = INTERVIEW_QUESTIONS_PROMPT.format(
            resume=resume_text,
            job_description=job_description
        )

        return self.generate_response(prompt)
    
    # -------------------------
    # Learning Roadmap
    # -------------------------
    def generate_roadmap(
        self,
        resume_text,
        job_description
    ):

        prompt = ROADMAP_PROMPT.format(
            resume=resume_text,
            job_description=job_description
        )

        return self.generate_response(prompt)
