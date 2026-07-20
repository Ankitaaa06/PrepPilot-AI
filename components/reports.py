import streamlit as st

from services.report_generator import generate_pdf_report


def reports_page():

    st.title("📊 AI Reports Dashboard")

    st.subheader("Generate Professional Interview Report")

    st.markdown("---")

    if not st.session_state.get("resume_text"):

        st.warning("⚠️ Please upload Resume first.")

        return

    # =============================
    # ATS Score
    # =============================

    ats_score = st.session_state.get("ats_score", 0)

    st.metric(
        "🎯 ATS Score",
        f"{ats_score}%"
    )

    st.progress(ats_score / 100)

    st.markdown("---")

    # =============================
    # Resume Match
    # =============================

    match_score = st.session_state.get(
        "resume_match",
        "Not Generated"
    )

    st.subheader("📈 Resume Match Score")

    st.write(match_score)

    st.markdown("---")

    # =============================
    # Missing Skills
    # =============================

    missing_skills = st.session_state.get(
        "missing_skills",
        []
    )

    st.subheader("📌 Missing Skills")

    if len(missing_skills) == 0:

        st.success("No Missing Skills 🎉")

    else:

        for skill in missing_skills:

            st.write(f"❌ {skill}")

    st.markdown("---")

    # =============================
    # AI Summary
    # =============================

    ai_summary = st.session_state.get(
        "ai_summary",
        "Not Generated"
    )

    st.subheader("🤖 AI Resume Summary")

    st.write(ai_summary)

    st.markdown("---")

    # =============================
    # Interview Questions
    # =============================

    interview_questions = st.session_state.get(
        "interview_questions",
        "Not Generated"
    )

    st.subheader("🎤 Interview Questions")

    st.markdown(interview_questions)

    st.markdown("---")

    # =============================
    # Generate Report
    # =============================

    if st.button("📄 Generate PDF Report"):

        pdf_path = generate_pdf_report(

            user_name=st.session_state.user_name,

            ats_score=ats_score,

            missing_skills=missing_skills,

            ai_summary=ai_summary,

            match_score=match_score,

            interview_questions=interview_questions

        )

        st.success("✅ PDF Generated Successfully!")

        with open(pdf_path, "rb") as file:

            st.download_button(

                label="⬇️ Download Report",

                data=file,

                file_name="PrepPilot_Report.pdf",

                mime="application/pdf"

            )