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
