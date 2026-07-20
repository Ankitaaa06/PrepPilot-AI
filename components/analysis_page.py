import streamlit as st

from services.analysis import calculate_ats_score
from services.skill_matcher import get_missing_keywords

from services.ai_analyzer import (
    analyze_resume,
    calculate_match_score
)


def analysis_page():

    st.title("📊 Resume Analysis")

    if not (
        st.session_state.get("resume_text")
        and st.session_state.get("jd_text")
    ):

        st.info("📄 Please upload Resume and Job Description first.")

        return

    # ================= ATS =================

    ats_score = calculate_ats_score(
        st.session_state.resume_text,
        st.session_state.jd_text
    )

    st.session_state.ats_score = ats_score

    st.subheader("🎯 ATS Analysis")

    st.progress(ats_score / 100)

    st.metric(
        "ATS Score",
        f"{ats_score}%"
    )

    if ats_score >= 80:
        st.success("🎉 Excellent Match!")

    elif ats_score >= 60:
        st.warning("👍 Good Match!")

    else:
        st.error("❌ Needs Improvement!")

    # ================= Missing Skills =================

    st.markdown("---")

    st.subheader("📌 Missing Skills")

    missing_skills = get_missing_keywords(
        st.session_state.resume_text,
        st.session_state.jd_text
    )

    if len(missing_skills) == 0:

        st.success("No major skills missing 🎉")

    else:

        for skill in missing_skills:

            st.write(f"❌ {skill}")

    # ================= AI Resume Analysis =================

    st.markdown("---")

    st.subheader("🤖 AI Resume Analysis")

    with st.spinner("Analyzing Resume..."):

        try:

            ai_response = analyze_resume(
                st.session_state.resume_text,
                st.session_state.jd_text
            )

            st.markdown(ai_response)

        except Exception as e:

            st.error("AI Analysis Failed!")

            st.exception(e)

    # ================= Resume Match Score =================

    st.markdown("---")

    st.subheader("🎯 Resume Match Score")

    with st.spinner("Calculating Match Score..."):

        try:

            result = calculate_match_score(
                st.session_state.resume_text,
                st.session_state.jd_text
            )

            st.markdown(result)

        except Exception as e:

            st.error("Match Score Failed!")

            st.exception(e)