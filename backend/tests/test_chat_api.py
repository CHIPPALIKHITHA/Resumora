from fastapi.testclient import TestClient

from app import config
from app.main import app

client = TestClient(app)

ANSWERS = [
    'Test Student',
    'test@example.com',
    '9876543210',
    'B.Tech CSE, SRM IST, 2022-2026, 8.5',
    'Python, SQL, Git',
    'Air Quality | Python, SQL | Built a pipeline for 50000 records; Cut effort by 40%',
    'skip',
]


def test_guided_flow_builds_a_resume(monkeypatch):
    monkeypatch.setattr(config, 'ANTHROPIC_API_KEY', '')
    messages = []
    r = client.post('/chat', json={'messages': messages, 'draft': {}}).json()
    assert r['mode'] == 'guided'
    for answer in ANSWERS:
        messages.append({'role': 'assistant', 'content': r['reply']})
        messages.append({'role': 'user', 'content': answer})
        r = client.post('/chat', json={'messages': messages, 'draft': r['draft']}).json()
    assert r['ready'] is True
    assert r['draft']['name'] == 'Test Student'
    assert r['draft']['projects'][0]['name'] == 'Air Quality'


def test_bad_email_asks_again(monkeypatch):
    monkeypatch.setattr(config, 'ANTHROPIC_API_KEY', '')
    messages = [
        {'role': 'assistant', 'content': 'What is your email address?'},
        {'role': 'user', 'content': 'not-an-email'},
    ]
    r = client.post('/chat', json={'messages': messages, 'draft': {'name': 'A B'}}).json()
    # draft lacks phone/email, so the first missing field is email
    assert r['draft']['email'] is None
    assert 'valid' in r['reply'].lower()
