import streamlit as st
import plotly.graph_objects as go

from utils.session_state import initialize_session_state

initialize_session_state()

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
    st.markdown("## 🎯 Overall ATS Score")

    score_color = "#22C55E"

    if ats_score < 80:
        score_color = "#F59E0B"

    if ats_score < 60:
        score_color = "#EF4444"

    st.markdown(
        f"""
        <div style="
            background:#1E293B;
            padding:30px;
            border-radius:20px;
            text-align:center;
            margin-bottom:25px;
            border:1px solid #334155;
        ">
            <h1 style="color:{score_color};font-size:60px;margin:0;">
                {ats_score}%
            </h1>
            <h3 style="color:white;">
                Resume Match Score
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Gauge Chart
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=ats_score,
            title={"text": "ATS Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#3B82F6"},
                "steps": [
                    {"range": [0, 50], "color": "#EF4444"},
                    {"range": [50, 80], "color": "#F59E0B"},
                    {"range": [80, 100], "color": "#22C55E"},
                ],
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("📊 Score Breakdown")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.metric(
            "🛠 Skills",
            f"{result['skill_score']}%"
        )

    with col2:
        st.metric(
            "🔑 Keywords",
            f"{result['keyword_score']}%"
        )

    with col3:
        st.metric(
            "💼 Experience",
            f"{result['experience_score']}%"
        )

    with col4:
        st.metric(
            "🎓 Education",
            f"{result['education_score']}%"
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

        st.success("### 🤖 AI Resume Analysis")

        st.markdown(st.session_state.ai_analysis)

    else:

        st.warning(
            "Upload Resume and Job Description First"
        )