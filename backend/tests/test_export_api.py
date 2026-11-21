from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_export_pdf_endpoint(good_resume):
    r = client.post('/export/pdf', json=good_resume.model_dump())
    assert r.status_code == 200
    assert r.headers['content-type'] == 'application/pdf'
    assert r.content.startswith(b'%PDF')


def test_export_docx_endpoint(good_resume):
    r = client.post('/export/docx', json=good_resume.model_dump())
    assert r.status_code == 200
    assert 'wordprocessingml' in r.headers['content-type']
    assert r.content[:2] == b'PK'
