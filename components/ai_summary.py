import streamlit as st


def ai_summary_page():

    st.title("🤖 AI Resume Summary")

    summary = st.session_state.get("ai_summary")

    if summary:

        st.markdown(summary)

    else:

        st.warning("Generate AI Analysis first.")