import streamlit as st
import plotly.graph_objects as go

from utils.ats_score import ATSScorer
from utils.gemini_client import GeminiClient

st.title("📊 Resume Analysis Dashboard")

if (
    st.session_state.resume_text
    and
    st.session_state.job_description
):

    scorer = ATSScorer()

    result = scorer.calculate_ats_score(
        st.session_state.resume_text,
        st.session_state.job_description
    )

    st.session_state.ats_result = result

    ats_score = result["final_ats_score"]

    # ATS Metric
    st.metric(
        label="ATS Score",
        value=f"{ats_score}%"
    )

    # Gauge Chart
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=ats_score,
            title={"text": "ATS Score"},
            gauge={
                "axis": {"range": [0, 100]}
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Score Breakdown")

    st.write("Skill Match")
    st.progress(
        int(result["skill_score"])
    )

    st.write("Keyword Match")
    st.progress(
        int(result["keyword_score"])
    )

    st.write("Experience Match")
    st.progress(
        int(result["experience_score"])
    )

    st.write("Education Match")
    st.progress(
        int(result["education_score"])
    )

    with st.expander(
        "View Detailed Scores"
    ):
        st.json(result)

    
    st.divider()

    st.subheader("🤖 AI Resume Analysis")

    if st.button("Generate AI Analysis"):

        with st.spinner(
            "Gemini is analyzing resume..."
        ):

            client = GeminiClient()

            analysis = client.analyze_resume(
                st.session_state.resume_text,
                st.session_state.job_description
            )

            st.session_state.ai_analysis = analysis

    if st.session_state.ai_analysis:

        st.markdown(
            st.session_state.ai_analysis
        )

else:

    st.warning(
        "Upload Resume and Job Description First"
    )