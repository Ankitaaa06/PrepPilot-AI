from openai import OpenAI
from dotenv import load_dotenv
import os

from services.vector_store import load_vector_store

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def ask_chatbot(resume_text, jd_text, user_question):

    try:

        vector_store = load_vector_store()

        docs = vector_store.similarity_search(
            user_question,
            k=3
        )

        retrieved_context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

    except Exception:

        retrieved_context = resume_text

    prompt = f"""
You are PrepPilot AI, an intelligent Interview Preparation Assistant and Career Mentor.

You have access to:

1. Relevant Resume Context retrieved using RAG
2. Job Description

Rules:

- ALWAYS use the retrieved resume context first.
- Use the Job Description whenever relevant.
- If the user asks about career guidance, interview preparation,
internships, projects, DSA, programming or resume improvement,
you may also use your own knowledge.

Never invent resume information.

If something is not present in the retrieved context,
clearly mention that before giving general advice.

==============================
Retrieved Resume Context
==============================

{retrieved_context}

==============================
Job Description
==============================

{jd_text}

==============================
User Question
==============================

{user_question}
"""

    try:

        response = client.chat.completions.create(

            model="openai/gpt-4o-mini",

            messages=[
                {
                    "role": "system",
                    "content": """
You are PrepPilot AI.

You are:
- Career Mentor
- Resume Reviewer
- Technical Interviewer
- HR Coach
- AI Mentor

Use retrieved context first.
Then use your own knowledge whenever appropriate.
"""
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

        return f"❌ Error:\n\n{e}"