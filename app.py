import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load CSS
# -----------------------------
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

with st.sidebar:
    st.markdown("## 🤖 AI Resume Analyzer")
    st.caption("Interview Coach & ATS Optimizer")

    st.divider()

    st.success("🚀 Powered by Gemini AI")

    st.divider()

    st.markdown(
        """
        ### Features

        ✅ Resume Parsing

        ✅ ATS Score

        ✅ AI Analysis

        ✅ Interview Questions

        ✅ Learning Roadmap

        ✅ PDF Report
        """
    )

    st.divider()

    st.caption("Made by Isha Manoria")

# -----------------------------
# Session State
# -----------------------------
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

# -----------------------------
# Hero Section
# -----------------------------
st.markdown(
    """
    <div class="hero-title">
        🤖 AI Resume Analyzer
    </div>

    <div class="hero-subtitle">
        ATS Scoring • Gemini AI • Interview Coach • Learning Roadmap
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Welcome Card
# -----------------------------
st.markdown(
    """
<div class="glass-card">

<h1>🚀 Welcome</h1>

<p>Upload your resume, paste a job description, and receive:</p>

<ul>
<li>✅ ATS Compatibility Score</li>
<li>✅ AI Resume Analysis</li>
<li>✅ Missing Skills Detection</li>
<li>✅ Personalized Learning Roadmap</li>
<li>✅ AI Interview Questions</li>
<li>✅ Professional PDF Report</li>
</ul>

</div>
""",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Feature Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-value">ATS</div>
            <div class="metric-label">
                Resume Match Scoring
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-value">AI</div>
            <div class="metric-label">
                Gemini Resume Analysis
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-value">PDF</div>
            <div class="metric-label">
                Professional Report
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.info(
    "👈 Use the sidebar to navigate through the application."
)