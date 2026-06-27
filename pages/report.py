import streamlit as st

from utils.gemini_client import GeminiClient
from utils.report_generator import generate_pdf_report

st.title("📑 Final Report & Learning Roadmap")

if (
    st.session_state.resume_text
    and
    st.session_state.job_description
):

    if st.button(
        "Generate Learning Roadmap"
    ):

        with st.spinner(
            "Generating roadmap..."
        ):

            client = GeminiClient()

            roadmap = client.generate_roadmap(
                st.session_state.resume_text,
                st.session_state.job_description
            )
            
            st.session_state.roadmap = roadmap

    if st.session_state.roadmap:

        st.subheader("📚 Personalized Roadmap")

        st.markdown(
            st.session_state.roadmap
        )

        st.divider()

if st.button(
    "Generate PDF Report"
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

    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.download_button(
        label="⬇ Download PDF Report",
        data=pdf_bytes,
        file_name="AI_Resume_Report.pdf",
        mime="application/pdf"  
    )

else:

    st.warning(
        "Upload Resume and Job Description First"
    )