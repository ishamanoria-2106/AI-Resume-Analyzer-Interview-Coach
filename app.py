import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "ats_result" not in st.session_state:
    st.session_state.ats_result = None

if "ai_analysis" not in st.session_state:
    st.session_state.ai_analysis = ""

if "interview_questions" not in st.session_state:
    st.session_state.interview_questions = ""

if "roadmap" not in st.session_state:
    st.session_state.roadmap = ""

st.title("📄 AI Resume Analyzer & Interview Coach")

st.markdown("""
Analyze resumes against job descriptions using ATS scoring,
embeddings, and Gemini AI.
""")