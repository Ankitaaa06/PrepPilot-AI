import streamlit as st


def ats_analysis_page():

    st.title("🎯 ATS Analysis")

    if st.session_state.get("ats_score") is not None:

        score = st.session_state.get("ats_score", 0)

        st.progress(score / 100)

        st.metric(
            "ATS Score",
            f"{score}%"
        )

        if score >= 80:
            st.success("🎉 Excellent Match!")

        elif score >= 60:
            st.warning("👍 Good Match!")

        else:
            st.error("❌ Needs Improvement!")

    else:

        st.warning("Generate AI Analysis first.")