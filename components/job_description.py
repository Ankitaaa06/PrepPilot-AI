import streamlit as st


def job_description_page():

    st.title("💼 Job Description")

    if st.session_state.get("jd_text"):

        st.text_area(
            "Job Description",
            st.session_state.jd_text,
            height=500
        )

    else:

        st.warning("Please upload Job Description from Quick Actions.")