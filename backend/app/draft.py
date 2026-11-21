from typing import Optional

from pydantic import BaseModel

from app.schema import Education, Experience, Project, Resume


class ResumeDraft(BaseModel):
    """A resume being built in conversation. Every field is optional."""

    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    summary: Optional[str] = None
    education: list[Education] = []
    experience: list[Experience] = []
    projects: list[Project] = []
    skills: list[str] = []

    def to_resume(self) -> Resume:
        data = self.model_dump()
        data['summary'] = data['summary'] or None
        return Resume(**data)


def missing_fields(d: ResumeDraft) -> list[str]:
    missing = []
    for key in ('name', 'email', 'phone'):
        if not getattr(d, key):
            missing.append(key)
    if not d.education:
        missing.append('education')
    if not d.skills:
        missing.append('skills')
    if not d.projects and not d.experience:
        missing.append('projects')
    if d.summary is None:
        missing.append('summary')
    return missing
