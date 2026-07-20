import streamlit as st

from services.interview_generator import generate_interview_questions
from services.answer_evaluator import evaluate_answer


def interview_page():

    st.title("🎤 AI Interview Preparation")

    st.subheader("Generate Personalized Interview Questions")

    st.markdown("---")

    # ================= Check Upload =================

    if (
        not st.session_state.get("resume_text")
        or not st.session_state.get("jd_text")
    ):

        st.warning("⚠️ Please upload Resume and Job Description first from Quick Actions.")

        return

    # ================= Settings =================

    question_type = st.selectbox(
        "Question Type",
        [
            "HR",
            "Technical",
            "Coding",
            "Mixed"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    num_questions = st.selectbox(
        "Number of Questions",
        [
            5,
            10,
            15
        ]
    )

    st.markdown("---")

    # ================= Generate Questions =================

    if st.button("🚀 Generate Interview Questions"):

        with st.spinner("Generating AI Interview Questions..."):

            questions = generate_interview_questions(
                st.session_state.resume_text,
                st.session_state.jd_text,
                question_type,
                difficulty,
                num_questions
            )

            st.session_state.interview_questions = questions

    # ================= Show Questions =================

    if st.session_state.get("interview_questions"):

        st.success("✅ Interview Questions Generated Successfully!")

        st.markdown(st.session_state.interview_questions)

        st.markdown("---")

        st.subheader("✍️ Practice Your Answer")

        question = st.text_area(
            "Paste one interview question here",
            height=120
        )

        answer = st.text_area(
            "Write your answer",
            height=220
        )

        if st.button("🤖 Evaluate My Answer"):

            if question.strip() == "" or answer.strip() == "":

                st.warning("Please enter both Question and Answer.")

            else:

                with st.spinner("Evaluating your answer..."):

                    feedback = evaluate_answer(
                        question,
                        answer
                    )

                st.success("✅ Evaluation Completed!")

                st.markdown(feedback)