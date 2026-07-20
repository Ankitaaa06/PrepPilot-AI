import streamlit as st
import matplotlib.pyplot as plt


def analytics_page():

    st.title("📊 Analytics Dashboard")

    ats = st.session_state.get("ats_score", 0)

    missing = len(
        st.session_state.get(
            "missing_skills",
            []
        )
    )

    readiness = min(
        100,
        ats + 10
    )

    # ================= Metrics =================

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "ATS Score",
            f"{ats}%"
        )

    with c2:
        st.metric(
            "Missing Skills",
            missing
        )

    with c3:
        st.metric(
            "Interview Readiness",
            f"{readiness}%"
        )

    st.markdown("---")

    # ================= Progress =================

    st.subheader("Overall Progress")

    st.progress(ats / 100)

    st.markdown("---")

    # ================= Pie Chart =================

    fig, ax = plt.subplots()

    ax.pie(
        [ats, 100 - ats],
        labels=["Matched", "Missing"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Resume Matching")

    st.pyplot(fig)

    st.markdown("---")

    # ================= Summary =================

    st.subheader("AI Insights")

    if ats >= 80:

        st.success(
            "Excellent Resume. Very good internship readiness."
        )

    elif ats >= 60:

        st.warning(
            "Good Resume. Add a few missing skills."
        )

    else:

        st.error(
            "Resume needs significant improvement."
        )