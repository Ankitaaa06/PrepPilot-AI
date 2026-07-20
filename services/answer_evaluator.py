from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def evaluate_answer(question, answer):

    prompt = f"""
You are a Senior Technical Interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer professionally.

Return ONLY in this format.

# Overall Score
X/10

# Strengths
- Point 1
- Point 2

# Weaknesses
- Point 1
- Point 2

# Ideal Answer
Write a model interview answer.

# Interview Tips
Give 3-5 practical tips to improve this answer.
"""

    try:

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

        return f"❌ Error:\n\n{e}"