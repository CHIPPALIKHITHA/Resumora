import logging

from fastapi import APIRouter

from app import config
from app.chat_models import ChatRequest, ChatResponse
from app.draft import missing_fields
from app.services.guided import guided_turn, next_question
from app.services.llm_service import llm_turn

router = APIRouter()
log = logging.getLogger(__name__)

GREETING = "Hi! I'm Resumora. I'll help you build an ATS-friendly resume."


@router.post('/chat', response_model=ChatResponse)
def chat(req: ChatRequest):
    draft = req.draft.model_copy(deep=True)
    mode = 'ai' if config.ANTHROPIC_API_KEY else 'guided'
    last = req.messages[-1] if req.messages else None
    user_text = last.content if last and last.role == 'user' else None

    if not req.messages:
        reply = f'{GREETING} {next_question(draft)}'
    elif mode == 'ai':
        try:
            reply, draft = llm_turn(req.messages, draft)
        except Exception:
            log.exception('Claude call failed, using guided flow')
            mode = 'guided'
            reply = guided_turn(draft, user_text)
    else:
        reply = guided_turn(draft, user_text)

    missing = missing_fields(draft)
    return ChatResponse(reply=reply, draft=draft, missing=missing, mode=mode, ready=not missing)
