import streamlit as st

from database.database import verify_user


def login_page():

    st.title("🔐 Login")

    email = st.text_input("📧 Email")

    password = st.text_input(
        "🔑 Password",
        type="password"
    )

    if st.button("Login"):

        user = verify_user(
            email,
            password
        )

        if user:

            st.session_state.logged_in = True
            st.session_state.user_name = user[1]

            st.success("Login Successful ✅")

        else:

            st.error("Invalid Email or Password")