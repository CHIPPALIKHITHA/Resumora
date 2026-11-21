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
