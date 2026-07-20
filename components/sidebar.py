import streamlit as st


def sidebar():

    with st.sidebar:

        st.title("🤖 PrepPilot AI")

        st.success(f"👋 {st.session_state.user_name}")

        st.markdown("---")

        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "⚡ Quick Actions",
                "📄 Resume",
                "💼 Job Description",
                "🎯 ATS Analysis",
                "📌 Missing Skills",
                "🤖 AI Resume Summary",
                "📊 Resume Match Score",
                "📈 Analytics Dashboard",
                "🎤 Interview Preparation",
                "💬 AI Chatbot",
                "📑 Reports"
            ]
        )

        st.markdown("---")

        logout = st.button("🚪 Logout")

    return page, logout