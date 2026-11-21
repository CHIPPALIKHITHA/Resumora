from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_analyze_endpoint(good_resume):
    r = client.post('/analyze', json=good_resume.model_dump())
    assert r.status_code == 200
    assert r.json()['score'] == 100
