from app.schema import Resume
from app.services.pdf_builder import build_pdf


def test_build_pdf_returns_pdf_bytes(good_resume):
    assert build_pdf(good_resume).startswith(b'%PDF')


def test_special_characters_do_not_crash(good_resume):
    r = good_resume.model_copy(deep=True)
    r.projects[0].name = 'R&D <Tool>'
    assert build_pdf(r).startswith(b'%PDF')


def test_required_fields_only():
    r = Resume(name='A B', email='a@b.com', phone='9999999999')
    assert build_pdf(r).startswith(b'%PDF')
