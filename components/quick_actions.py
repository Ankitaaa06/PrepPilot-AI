import streamlit as st

from services.pdf_service import (
    save_uploaded_file,
    extract_text_from_pdf
)

from services.text_processing import clean_resume_text
from services.chunking import split_resume_text
from services.vector_store import create_vector_store

from services.analysis import calculate_ats_score
from services.skill_matcher import get_missing_keywords

from services.ai_analyzer import (
    analyze_resume,
    calculate_match_score
)


def quick_actions():

    st.title("⚡ Quick Actions")
    st.write("Upload your Resume and Job Description.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    # ================= Resume Upload =================

    with col1:

        uploaded_resume = st.file_uploader(
            "📄 Upload Resume",
            type=["pdf"],
            key="resume_upload"
        )

        if uploaded_resume:

            path = save_uploaded_file(
                uploaded_resume,
                "resumes"
            )

            resume_text = extract_text_from_pdf(path)
            resume_text = clean_resume_text(resume_text)

            chunks = split_resume_text(resume_text)

            create_vector_store(chunks)

            st.session_state.resume_uploaded = True
            st.session_state.resume_text = resume_text
            st.session_state.resume_chunks = chunks

            st.success("✅ Resume Uploaded Successfully!")

    # ================= JD Upload =================

    with col2:

        uploaded_jd = st.file_uploader(
            "💼 Upload Job Description",
            type=["pdf"],
            key="jd_upload"
        )

        if uploaded_jd:

            jd_path = save_uploaded_file(
                uploaded_jd,
                "job_descriptions"
            )

            jd_text = extract_text_from_pdf(jd_path)
            jd_text = clean_resume_text(jd_text)

            st.session_state.jd_text = jd_text

            st.success("✅ Job Description Uploaded!")

    # ================= Generate Analysis =================

    if (
        st.session_state.get("resume_text")
        and
        st.session_state.get("jd_text")
    ):

        st.markdown("---")

        if st.button(
            "🚀 Generate Complete AI Analysis",
            use_container_width=True
        ):

            with st.spinner("Analyzing Resume..."):

                # ATS

                ats_score = calculate_ats_score(
                    st.session_state.resume_text,
                    st.session_state.jd_text
                )

                st.session_state.ats_score = ats_score

                # Missing Skills

                missing_skills = get_missing_keywords(
                    st.session_state.resume_text,
                    st.session_state.jd_text
                )

                st.session_state.missing_skills = missing_skills

                # AI Summary

                ai_summary = analyze_resume(
                    st.session_state.resume_text,
                    st.session_state.jd_text
                )

                st.session_state.ai_summary = ai_summary

                # Resume Match

                resume_match = calculate_match_score(
                    st.session_state.resume_text,
                    st.session_state.jd_text
                )

                st.session_state.resume_match = resume_match

                st.success("🎉 AI Analysis Generated Successfully!")

        # ================= Quick Preview =================

        if st.session_state.get("ats_score"):

            st.markdown("---")

            st.subheader("📊 Quick Preview")

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "ATS Score",
                    f"{st.session_state.ats_score}%"
                )

            with c2:

                st.metric(
                    "Missing Skills",
                    len(
                        st.session_state.get(
                            "missing_skills",
                            []
                        )
                    )
                )

            st.success(
                "✅ Now open pages from the sidebar to see complete reports."
            )

    else:

        st.info(
            "Upload Resume and Job Description first."
        )