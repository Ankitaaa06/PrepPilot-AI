import streamlit as st

from services.chatbot import ask_chatbot


def chatbot_page():

    st.title("💬 AI Chatbot")

    st.subheader("Ask Anything About Your Resume & Job Description")

    st.markdown("---")

    # Check Resume & JD

    if (
        not st.session_state.get("resume_text")
        or not st.session_state.get("jd_text")
    ):

        st.warning(
            "⚠️ Please upload Resume and Job Description first from Quick Actions."
        )

        return

    # Chat History

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    # Display Previous Chats

    for chat in st.session_state.chat_history:

        with st.chat_message(chat["role"]):

            st.markdown(chat["content"])

    # User Input

    prompt = st.chat_input("Ask something about your Resume or Job Description...")

    if prompt:

        # User Message

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        # AI Response

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = ask_chatbot(
                    st.session_state.resume_text,
                    st.session_state.jd_text,
                    prompt
                )

                st.markdown(response)

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.chat_history = []

        st.rerun()