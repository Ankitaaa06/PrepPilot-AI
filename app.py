import streamlit as st

from database.database import (
    create_connection,
    create_users_table
)

from authentication.login import login_page
from authentication.signup import signup_page

from components.sidebar import sidebar
from components.dashboard import dashboard
from components.quick_actions import quick_actions
from components.resume import resume_page
from components.job_description import job_description_page
from components.ats_analysis import ats_analysis_page
from components.missing_skills import missing_skills_page
from components.ai_summary import ai_summary_page
from components.resume_match import resume_match_page
from components.analytics import analytics_page
from components.interview import interview_page
from components.chatbot import chatbot_page
from components.reports import reports_page


st.set_page_config(
    page_title="PrepPilot AI",
    page_icon="🤖",
    layout="wide"
)

create_connection()
create_users_table()

# ================= Session State =================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# ================= Logged In =================

if st.session_state.logged_in:

    page, logout = sidebar()

    if logout:
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        st.rerun()

    if page == "🏠 Dashboard":
        dashboard()

    elif page == "⚡ Quick Actions":
        quick_actions()

    elif page == "📄 Resume":
        resume_page()

    elif page == "💼 Job Description":
        job_description_page()

    elif page == "🎯 ATS Analysis":
        ats_analysis_page()

    elif page == "📌 Missing Skills":
        missing_skills_page()

    elif page == "🤖 AI Resume Summary":
        ai_summary_page()

    elif page == "📊 Resume Match Score":
        resume_match_page()

    elif page == "📈 Analytics Dashboard":
        analytics_page()

    elif page == "🎤 Interview Preparation":
        interview_page()

    elif page == "💬 AI Chatbot":
        chatbot_page()

    elif page == "📑 Reports":
        reports_page()

# ================= Login / Signup =================

else:

    st.sidebar.title("🤖 PrepPilot AI")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Login",
            "Sign Up"
        ]
    )

    if menu == "Login":
        login_page()

    else:
        signup_page()