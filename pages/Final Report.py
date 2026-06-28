import streamlit as st

from utils.gemini_client import GeminiClient
from utils.report_generator import generate_pdf_report

# ------------------------------------------------
# Hero Section
# ------------------------------------------------

st.markdown(
    """
    <div class="hero-title">
        📑 Final Report
    </div>

    <div class="hero-subtitle">
        Generate your personalized learning roadmap and download a professional resume analysis report.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ------------------------------------------------
# Check Inputs
# ------------------------------------------------

if (
    st.session_state.resume_text
    and
    st.session_state.job_description
):

    st.success("✅ Resume and Job Description are ready.")

    # --------------------------------------------
    # Generate Roadmap
    # --------------------------------------------

    if st.button(
        "📚 Generate Personalized Learning Roadmap",
        use_container_width=True
    ):

        with st.spinner(
            "Generating your personalized roadmap..."
        ):

            client = GeminiClient()

            roadmap = client.generate_roadmap(
                st.session_state.resume_text,
                st.session_state.job_description
            )

            st.session_state.roadmap = roadmap

    # --------------------------------------------
    # Roadmap Display
    # --------------------------------------------

    if st.session_state.get("roadmap"):

        st.divider()

        st.subheader("📚 Personalized Learning Roadmap")

        st.markdown(
            f"""
            <div class="glass-card">

            {st.session_state.roadmap}

            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # --------------------------------------------
    # Report Status
    # --------------------------------------------

    st.subheader("📋 Report Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "ATS Analysis",
            "✅ Ready" if st.session_state.get("ats_result") else "❌ Missing"
        )

        st.metric(
            "AI Analysis",
            "✅ Ready" if st.session_state.get("ai_analysis") else "❌ Missing"
        )

    with col2:
        st.metric(
            "Interview Questions",
            "✅ Ready" if st.session_state.get("interview_questions") else "❌ Missing"
        )

        st.metric(
            "Learning Roadmap",
            "✅ Ready" if st.session_state.get("roadmap") else "❌ Missing"
        )

    st.divider()

    # --------------------------------------------
    # PDF Download
    # --------------------------------------------

    st.subheader("📄 Download Report")

    if st.button(
        "📥 Generate PDF Report",
        use_container_width=True
    ):

        ats_result = (
            st.session_state.ats_result
            if st.session_state.ats_result
            else {}
        )

        pdf_path = generate_pdf_report(
            ats_result,
            st.session_state.ai_analysis,
            st.session_state.interview_questions,
            st.session_state.roadmap
        )

        import os

        st.write("PDF Path:", pdf_path)
        st.write("Exists:", os.path.exists(pdf_path))

        if os.path.exists(pdf_path):
            st.write("Size:", os.path.getsize(pdf_path))

        with open(pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        st.success("✅ PDF Generated Successfully!")

        st.download_button(
            label="⬇ Download Professional Report",
            data=pdf_bytes,
            file_name="AI_Resume_Report.pdf",
            mime="application/pdf"
        )

else:

    st.warning(
        "⚠ Please upload your resume and job description first."
    )