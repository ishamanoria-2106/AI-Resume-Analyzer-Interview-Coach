import streamlit as st
import tempfile
import os

from utils.pdf_parser import parse_resume

st.title("📤 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            uploaded_file.read()
        )

        temp_path = temp_file.name

    result = parse_resume(temp_path)

    st.session_state.resume_text = (
        result["cleaned_text"]
    )

    st.success(
        "Resume Processed Successfully"
    )

if job_description:

    st.session_state.job_description = (
        job_description
    )

    st.success(
        "Job Description Saved"
    )