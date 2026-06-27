RESUME_ANALYSIS_PROMPT = """
Analyze the resume against the job description.

Return ONLY in the following format:

STRENGTHS
- point 1
- point 2
- point 3

WEAKNESSES
- point 1
- point 2
- point 3

MISSING SKILLS
- point 1
- point 2
- point 3

RECOMMENDATIONS
- point 1
- point 2
- point 3

Resume:
{resume}

Job Description:
{job_description}
"""


INTERVIEW_QUESTIONS_PROMPT = """
Generate interview questions.

Return ONLY in this format:

TECHNICAL QUESTIONS
1.
2.
3.
4.
5.

BEHAVIORAL QUESTIONS
1.
2.
3.
4.
5.

HR QUESTIONS
1.
2.
3.
4.
5.

Resume:
{resume}

Job Description:
{job_description}
"""


ROADMAP_PROMPT = """
Create a learning roadmap.

Return ONLY in this format:

SKILLS TO LEARN
- skill
- skill
- skill

30 DAY PLAN
- task
- task
- task

60 DAY PLAN
- task
- task
- task

90 DAY PLAN
- task
- task
- task

Resume:
{resume}

Job Description:
{job_description}
"""