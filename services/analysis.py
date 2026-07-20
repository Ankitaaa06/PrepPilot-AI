from difflib import SequenceMatcher


def calculate_ats_score(resume_text, job_description):

    resume = resume_text.lower()
    job = job_description.lower()

    score = SequenceMatcher(None, resume, job).ratio()

    return round(score * 100)


def get_missing_keywords(resume_text, job_description):

    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    missing = job_words - resume_words

    keywords = []

    for word in missing:

        word = word.strip(",.()[]{}")

        if len(word) > 3 and word.isalpha():
            keywords.append(word)

    return sorted(list(set(keywords)))[:20]