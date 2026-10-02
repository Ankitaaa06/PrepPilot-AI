from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("sk-or-v1-ad2...9c0") or st.secrets["sk-or-v1-ad2...9c0"],
)

# =====================================================
# AI Resume Analysis
# =====================================================

def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Reviewer.

IMPORTANT RULES:
- Do NOT invent or assume any information.
- Use ONLY the information present in the Resume and Job Description.
- If something is missing, write "Not Mentioned".

Resume:
{resume_text}

Job Description:
{job_description}

Analyze professionally.

Return in this format:

## Resume Summary

## Strengths

## Weaknesses

## Missing Skills

## ATS Improvement Tips

## Final Suggestions
"""

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


# =====================================================
# Resume Match Score
# =====================================================

def calculate_match_score(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Matching System.

Compare the Resume and Job Description.

Resume:
{resume_text}

Job Description:
{job_description}

Rules:
- Do NOT guess.
- Only compare using the provided content.

Return ONLY in this format:

# Resume Match Score
XX%

# Matching Skills
- skill
- skill
- skill

# Missing Skills
- skill
- skill
- skill

# Recommendation
Write 3-5 lines explaining how the candidate can improve the resume for this job.
"""

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