import streamlit as st


def missing_skills_page():

    st.title("📌 Missing Skills")

    skills = st.session_state.get("missing_skills", [])

    if skills:

        for skill in skills:

            st.error(f"❌ {skill}")

    else:

        st.success("🎉 No Missing Skills Found.")