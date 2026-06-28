import streamlit as st

from utils.session_state import initialize_session_state

initialize_session_state()

from utils.gemini_client import GeminiClient

# ------------------------------------------------
# Hero Section
# ------------------------------------------------

st.markdown(
    """
    <div class="hero-title">
        🎤 AI Interview Coach
    </div>

    <div class="hero-subtitle">
        Generate personalized interview questions based on your resume and target job.
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

    st.info(
        "🤖 Gemini AI will generate interview questions tailored to your resume and the selected job description."
    )

    # --------------------------------------------
    # Generate Button
    # --------------------------------------------

    if st.button(
        "🚀 Generate Interview Questions",
        use_container_width=True
    ):

        with st.spinner(
            "Generating personalized interview questions..."
        ):

            client = GeminiClient()

            questions = client.generate_interview_questions(
                st.session_state.resume_text,
                st.session_state.job_description
            )

            st.session_state.interview_questions = questions

    # --------------------------------------------
    # Display Questions
    # --------------------------------------------

    if st.session_state.get("interview_questions"):

        st.divider()

        st.subheader("📝 Personalized Interview Questions")

        st.success(
            "Practice these questions before your interview."
        )

        st.markdown(
            f"""
<div class="glass-card">

{st.session_state.interview_questions}

</div>
""",
            unsafe_allow_html=True
        )

        st.divider()

        st.info(
            """
### 💡 Interview Tips

✅ Answer using the STAR Method

✅ Be concise and structured

✅ Mention measurable achievements

✅ Relate your answers to the job description

✅ Practice aloud before your interview
"""
        )

else:

    st.warning(
        "⚠ Please upload your resume and job description first."
    )