from io import BytesIO

from docx import Document

from app.schema import Resume
from app.services.docx_builder import build_docx


def _read(data: bytes) -> Document:
    return Document(BytesIO(data))


def test_build_docx_contains_name(good_resume):
    doc = _read(build_docx(good_resume))
    assert any(good_resume.name in p.text for p in doc.paragraphs)


def test_docx_has_no_tables(good_resume):
    doc = _read(build_docx(good_resume))
    assert len(doc.tables) == 0


def test_required_fields_only():
    r = Resume(name='A B', email='a@b.com', phone='9999999999')
    assert build_docx(r)[:2] == b'PK'
