import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_openrouter_client():
    """
    Create the OpenRouter client only when needed.
    """

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        api_key = st.secrets.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not configured."
        )

    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )


def generate_interview_questions(
    resume_text,
    jd_text,
    question_type,
    difficulty,
    num_questions
):

    prompt = f"""
You are an expert technical interviewer.

Candidate Resume:
{resume_text}

Job Description:
{jd_text}

Generate {num_questions} {difficulty} level interview questions.

Question Type:
{question_type}

Instructions:

If HR:
- Ask HR/personality questions only.

If Technical:
- Ask technical questions based on Resume + JD.

If Coding:
- Ask DSA/programming questions relevant to skills.

If Mixed:
- Include HR + Technical + Coding questions.

Return in clean Markdown.

Example:

# HR Questions

1. Question
2. Question

# Technical Questions

1. Question
2. Question

# Coding Questions

1. Question
2. Question
"""

    try:

        client = get_openrouter_client()

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced software engineering "
                        "interviewer."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1200
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"