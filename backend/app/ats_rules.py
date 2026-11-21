import re

from pydantic import BaseModel

from app.schema import Resume


class Issue(BaseModel):
    section: str
    message: str
    penalty: int = 3


def check_contact(r: Resume) -> list[Issue]:
    issues = []
    digits = ''.join(c for c in r.phone if c.isdigit())
    if len(digits) < 10:
        issues.append(Issue(section='contact', message='Phone number looks incomplete (need 10+ digits).', penalty=5))
    if not r.linkedin:
        issues.append(Issue(section='contact', message='Add a LinkedIn URL.'))
    if not r.github:
        issues.append(Issue(section='contact', message='Add a GitHub URL (important for tech roles).'))
    return issues


def check_summary(r: Resume) -> list[Issue]:
    if not r.summary:
        return [Issue(section='summary', message='Add a 2-3 line professional summary.', penalty=5)]
    words = len(r.summary.split())
    if words < 20 or words > 70:
        return [Issue(section='summary', message='Keep the summary between 20 and 70 words.')]
    return []


ACTION_VERBS = {
    'built', 'developed', 'designed', 'led', 'optimized', 'implemented', 'created',
    'automated', 'reduced', 'improved', 'deployed', 'engineered', 'analyzed',
    'integrated', 'launched', 'managed', 'migrated', 'wrote', 'architected', 'delivered',
}


def _all_bullets(r: Resume):
    for e in r.experience:
        for b in e.bullets:
            yield e.role, b
    for p in r.projects:
        for b in p.bullets:
            yield p.name, b


def check_action_verbs(r: Resume) -> list[Issue]:
    issues = []
    for where, b in _all_bullets(r):
        words = b.split()
        if words and words[0].lower().strip(',.:;') not in ACTION_VERBS:
            issues.append(Issue(section=where, message=f"Start with a strong action verb: '{b[:50]}'", penalty=2))
    return issues


def check_metrics(r: Resume) -> list[Issue]:
    issues = []
    for where, b in _all_bullets(r):
        if not re.search(r'\d', b):
            issues.append(Issue(section=where, message=f"Add a number or metric (%, count, time): '{b[:50]}'", penalty=2))
    return issues


def check_bullet_length(r: Resume) -> list[Issue]:
    issues = []
    for where, b in _all_bullets(r):
        n = len(b.split())
        if n < 6 or n > 30:
            issues.append(Issue(section=where, message=f'Keep bullets between 6 and 30 words (this one has {n}).', penalty=1))
    return issues


def check_skills(r: Resume) -> list[Issue]:
    if len(r.skills) < 5:
        return [Issue(section='skills', message='List at least 5 relevant skills.', penalty=5)]
    return []
