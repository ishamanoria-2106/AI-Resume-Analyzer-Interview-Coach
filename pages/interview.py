import streamlit as st

from utils.gemini_client import GeminiClient

st.title("🎤 AI Interview Coach")

if (
    st.session_state.resume_text
    and
    st.session_state.job_description
):

    if st.button(
        "Generate Interview Questions"
    ):

        with st.spinner(
            "Generating questions..."
        ):

            client = GeminiClient()

            questions = (
                client.generate_interview_questions(
                    st.session_state.resume_text,
                    st.session_state.job_description
                )
            )

            st.session_state.interview_questions = (
                questions
            )

    if st.session_state.interview_questions:

        st.markdown(
            st.session_state.interview_questions
        )

else:

    st.warning(
        "Upload Resume and Job Description First"
    )