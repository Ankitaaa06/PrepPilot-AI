import streamlit as st

from database.database import (
    user_exists,
    insert_user
)


def signup_page():

    st.title("📝 Sign Up")

    name = st.text_input(
        "👤 Full Name"
    )

    email = st.text_input(
        "📧 Email"
    )

    password = st.text_input(
        "🔑 Password",
        type="password"
    )

    confirm_password = st.text_input(
        "🔒 Confirm Password",
        type="password"
    )

    if st.button("Create Account"):

        if "" in [name, email, password, confirm_password]:
            st.warning("Please fill all fields.")

        elif password != confirm_password:
            st.error("Passwords do not match.")

        elif user_exists(email):
            st.error("Email already registered.")

        else:

            insert_user(
                name,
                email,
                password
            )

            st.success("Account Created Successfully! 🎉")