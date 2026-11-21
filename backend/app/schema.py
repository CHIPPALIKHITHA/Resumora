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


class Project(BaseModel):
    name: str
    tech: list[str] = []
    bullets: list[str] = []
    link: Optional[str] = None


class Resume(BaseModel):
    name: str
    email: EmailStr
    phone: str
    linkedin: Optional[str] = None
    github: Optional[str] = None
    summary: Optional[str] = None
    education: list[Education] = []
    experience: list[Experience] = []
    projects: list[Project] = []
    skills: list[str] = []
