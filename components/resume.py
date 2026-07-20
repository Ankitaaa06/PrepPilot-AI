import streamlit as st


def resume_page():

    st.title("📄 Resume")

    if st.session_state.get("resume_text"):

        st.text_area(
            "Resume Content",
            st.session_state.resume_text,
            height=500
        )

    else:

        st.warning("Please upload your Resume from Quick Actions.")