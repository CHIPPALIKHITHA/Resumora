from typing import Optional

from pydantic import BaseModel, EmailStr


class Education(BaseModel):
    institution: str
    degree: str
    start: str
    end: str
    cgpa: Optional[str] = None
