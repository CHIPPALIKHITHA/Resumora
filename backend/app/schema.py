from typing import Optional

from pydantic import BaseModel, EmailStr


class Education(BaseModel):
    institution: str
    degree: str
    start: str
    end: str
    cgpa: Optional[str] = None


class Experience(BaseModel):
    role: str
    company: str
    start: str
    end: str
    bullets: list[str] = []


class Project(BaseModel):
    name: str
    tech: list[str] = []
    bullets: list[str] = []
    link: Optional[str] = None
