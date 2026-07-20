import streamlit as st


def dashboard():

    st.title("🤖 PrepPilot AI")
    st.subheader("Your Personal AI Interview Coach")

    st.markdown("---")

    st.success(f"👋 Welcome, {st.session_state.user_name}")

    # ================= Metrics =================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📄 Resume",
            "Uploaded" if st.session_state.get("resume_uploaded") else "Not Uploaded"
        )

    with col2:
        st.metric(
            "🎯 ATS Score",
            f"{st.session_state.get('ats_score', 0)}%"
        )

    with col3:
        st.metric(
            "🎯 Resume Match",
            "Available" if st.session_state.get("resume_match") else "Pending"
        )

    with col4:
        st.metric(
            "📌 Missing Skills",
            len(st.session_state.get("missing_skills", []))
        )

    st.markdown("---")

    st.subheader("🚀 Project Overview")

    st.write(
        """
PrepPilot AI helps you prepare for placements by analyzing your resume,
comparing it with a Job Description, identifying missing skills,
calculating ATS score, generating AI-powered resume feedback,
and preparing you for technical as well as HR interviews.
"""
    )

    st.markdown("---")

    st.subheader("📋 Workflow")

    st.success("Step 1️⃣  → Go to **Quick Actions**")

    st.success("Step 2️⃣  → Upload Resume")

    st.success("Step 3️⃣  → Upload Job Description")

    st.success("Step 4️⃣  → Click **Generate Complete AI Analysis**")

    st.success("Step 5️⃣  → View reports from the Sidebar")

    st.markdown("---")

    st.subheader("✨ Features Available")

    feature1, feature2 = st.columns(2)

    with feature1:

        st.info("📄 Resume Viewer")

        st.info("💼 Job Description Viewer")

        st.info("🎯 ATS Analysis")

        st.info("📌 Missing Skills")

        st.info("🤖 AI Resume Summary")

    with feature2:

        st.info("🎯 Resume Match Score")

        st.info("🎤 Interview Preparation (Coming Soon)")

        st.info("💬 AI Chatbot (Coming Soon)")

        st.info("📊 Reports (Coming Soon)")

        st.info("📥 PDF Download (Coming Soon)")

    st.markdown("---")

    st.caption("© 2026 PrepPilot AI | Built using Python, Streamlit & OpenAI")