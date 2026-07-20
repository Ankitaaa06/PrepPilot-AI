import re


def extract_keywords(text):

    text = text.lower()

    words = re.findall(r"\b[a-zA-Z]+\b", text)

    return sorted(list(set(words)))


def match_skills(resume_text, jd_text):

    resume_skills = extract_keywords(resume_text)
    jd_skills = extract_keywords(jd_text)

    matched = []
    missing = []

    for skill in jd_skills:

        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing


def get_missing_keywords(resume_text, jd_text):

    _, missing = match_skills(resume_text, jd_text)

    return missing