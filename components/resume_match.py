import streamlit as st


def resume_match_page():

    st.title("🎯 Resume Match Score")

    result = st.session_state.get("resume_match")

    if result:

        st.markdown(result)

    else:

        st.warning("Generate AI Analysis first.")