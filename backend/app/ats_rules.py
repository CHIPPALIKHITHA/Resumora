import re

from pydantic import BaseModel

from app.schema import Resume


class Issue(BaseModel):
    section: str
    message: str
    penalty: int = 3
