import streamlit as st
from openai import OpenAI


def get_openrouter_client():
    api_key = st.secrets["OPENROUTER_API_KEY"]

    return OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )


def analyze_resume(resume_text, jd_text):

    prompt = f"""
You are an AI resume analysis assistant.

Analyze the following resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}

Provide:
1. Resume summary
2. Strengths
3. Weaknesses
4. Missing skills
5. Suggestions for improvement
"""

    try:
        client = get_openrouter_client()

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


def calculate_match_score(resume_text, jd_text):

    prompt = f"""
Compare this resume with this job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}

Return only a match score from 0 to 100.
"""

    try:
        client = get_openrouter_client()

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content.strip()

        digits = "".join(filter(str.isdigit, result))

        if digits:
            return min(int(digits), 100)

        return 0

    except Exception:
        return 0