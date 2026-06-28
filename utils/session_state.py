import streamlit as st

def initialize_session_state():

    defaults = {
        "resume_text": "",
        "job_description": "",
        "ats_result": {},
        "ai_analysis": "",
        "interview_questions": "",
        "roadmap": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value