import requests
import streamlit as st


def get_api_key():
    return st.secrets["OPENROUTER_API_KEY"].strip()


def call_openrouter(prompt):
    api_key = get_api_key()

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json",
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
        },
        timeout=120,
    )

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    data = response.json()

    return data["choices"][0]["message"]["content"]


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
        return call_openrouter(prompt)

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
        result = call_openrouter(prompt).strip()

        digits = "".join(filter(str.isdigit, result))

        if digits:
            return min(int(digits), 100)

        return 0

    except Exception:
        return 0