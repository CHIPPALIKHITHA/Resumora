from typing import Literal

from pydantic import BaseModel, Field

from app.draft import ResumeDraft


class ChatMessage(BaseModel):
    role: Literal['user', 'assistant']
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = []
    draft: ResumeDraft = Field(default_factory=ResumeDraft)


class ChatResponse(BaseModel):
    reply: str
    draft: ResumeDraft
    missing: list[str]
    mode: Literal['ai', 'guided']
    ready: bool
