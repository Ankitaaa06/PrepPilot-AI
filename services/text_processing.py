import re


def clean_resume_text(text):

    text = re.sub(r"\n+", "\n", text)

    text = re.sub(r"\t+", " ", text)

    text = re.sub(r" +", " ", text)

    text = text.strip()

    return text 