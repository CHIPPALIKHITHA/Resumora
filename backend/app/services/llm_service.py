import anthropic

from app import config
from app.chat_models import ChatMessage
from app.draft import ResumeDraft, missing_fields

SYSTEM = """You are Resumora, a friendly assistant that helps students build ATS-friendly resumes.
Rules:
- Ask for ONE missing section at a time and keep replies short.
- Save facts from the student's messages into the resume with the update_resume tool.
- Never invent employers, dates, numbers, or achievements. If a bullet lacks a number, ask for it.
- Write bullets that start with a strong action verb.
- When everything required is filled, write a 2-3 line summary using only the facts given, then tell the student they can download the resume or run the ATS check."""


def _tool() -> dict:
    schema = ResumeDraft.model_json_schema()
    defs = schema.pop('$defs', {})
    return {
        'name': 'update_resume',
        'description': 'Save the full updated resume draft and the reply to show the student.',
        'input_schema': {
            'type': 'object',
            'properties': {'draft': schema, 'reply': {'type': 'string'}},
            'required': ['draft', 'reply'],
            '$defs': defs,
        },
    }


def llm_turn(messages: list[ChatMessage], draft: ResumeDraft):
    client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)
    context = f'Current draft JSON: {draft.model_dump_json()}\nStill missing: {missing_fields(draft)}'
    response = client.messages.create(
        model=config.CLAUDE_MODEL,
        max_tokens=1500,
        system=SYSTEM + '\n\n' + context,
        tools=[_tool()],
        tool_choice={'type': 'tool', 'name': 'update_resume'},
        messages=[{'role': m.role, 'content': m.content} for m in messages],
    )
    for block in response.content:
        if block.type == 'tool_use':
            return block.input['reply'], ResumeDraft.model_validate(block.input['draft'])
    raise RuntimeError('Model returned no tool output')
