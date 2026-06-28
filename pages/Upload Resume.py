import streamlit as st
import tempfile

from utils.session_state import initialize_session_state

initialize_session_state()

from utils.pdf_parser import parse_resume

# ------------------------------------------------
# Hero Section
# ------------------------------------------------

st.markdown(
    """
    <div class="hero-title">
        📤 Upload Resume
    </div>

    <div class="hero-subtitle">
        Upload your resume and paste the job description to begin AI-powered analysis.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ------------------------------------------------
# Two Column Layout
# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 📄 Resume")

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

with col2:

    st.markdown("### 💼 Job Description")

    job_description = st.text_area(
        "Paste Job Description",
        height=350,
        placeholder="Paste the complete job description here..."
    )

# ------------------------------------------------
# Resume Processing
# ------------------------------------------------

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(uploaded_file.read())

        temp_path = temp_file.name

    result = parse_resume(temp_path)

    st.session_state.resume_text = result["cleaned_text"]

    st.success("✅ Resume Processed Successfully")

# ------------------------------------------------
# Save Job Description
# ------------------------------------------------

if job_description:

    st.session_state.job_description = job_description

    st.success("✅ Job Description Saved")

# ------------------------------------------------
# Summary Cards
# ------------------------------------------------

if (
    st.session_state.resume_text
    and
    st.session_state.job_description
):

    st.divider()

    st.subheader("📊 Input Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📄 Resume Length",
            f"{len(st.session_state.resume_text.split())} words"
        )

    with col2:

        st.metric(
            "💼 Job Description Length",
            f"{len(st.session_state.job_description.split())} words"
        )

# ------------------------------------------------
# Analyze Button
# ------------------------------------------------

st.divider()

if st.button(
    "🚀 Analyze Resume",
    use_container_width=True
):

    if (
        st.session_state.resume_text
        and
        st.session_state.job_description
    ):

        st.success(
            "✅ Resume is ready for analysis.\n\nUse the **Resume Analysis** page from the sidebar."
        )

    else:

        st.warning(
            "⚠ Please upload a resume and paste a job description first."
        )