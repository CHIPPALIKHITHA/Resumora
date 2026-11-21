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
