import re

from app.draft import ResumeDraft, missing_fields
from app.schema import Education, Project

QUESTIONS = {
    'name': 'What is your full name?',
    'email': 'What is your email address?',
    'phone': 'What is your phone number?',
    'education': 'Tell me your education as: Degree, Institution, Start-End, CGPA (e.g. B.Tech CSE, SRM IST, 2022-2026, 8.5)',
    'skills': 'List your skills separated by commas (e.g. Python, SQL, Git).',
    'projects': 'Describe a project as: Name | tech1, tech2 | achievement 1; achievement 2',
    'summary': "Write a 2-3 line summary about yourself, or type 'skip'.",
}

EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')


def apply_answer(d: ResumeDraft, field: str, text: str):
    """Store the answer in the draft. Returns an error message, or None if OK."""
    text = text.strip()
    if field == 'email':
        if not EMAIL_RE.match(text):
            return 'That email does not look valid. Please try again.'
        d.email = text
    elif field in ('name', 'phone'):
        setattr(d, field, text)
    elif field == 'summary':
        d.summary = '' if text.lower() == 'skip' else text
    elif field == 'skills':
        d.skills = [s.strip() for s in text.split(',') if s.strip()]
    elif field == 'education':
        parts = [p.strip() for p in text.split(',')]
        if len(parts) < 3:
            return 'Please use: Degree, Institution, Start-End, CGPA'
        years = re.split(r'\s*[-\u2013]\s*', parts[2])
        if len(years) != 2:
            return 'Years should look like 2022-2026'
        d.education.append(Education(
            degree=parts[0], institution=parts[1], start=years[0], end=years[1],
            cgpa=parts[3] if len(parts) > 3 else None,
        ))
    elif field == 'projects':
        parts = [p.strip() for p in text.split('|')]
        if len(parts) < 3:
            return 'Please use: Name | tech1, tech2 | achievement 1; achievement 2'
        d.projects.append(Project(
            name=parts[0],
            tech=[t.strip() for t in parts[1].split(',') if t.strip()],
            bullets=[b.strip() for b in parts[2].split(';') if b.strip()],
        ))
    return None
