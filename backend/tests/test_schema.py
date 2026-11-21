import pytest
from pydantic import ValidationError

from app.schema import Resume


def test_minimal_resume_is_valid():
    r = Resume(name='A B', email='a@b.com', phone='9999999999')
    assert r.skills == []


def test_invalid_email_rejected():
    with pytest.raises(ValidationError):
        Resume(name='A B', email='not-an-email', phone='9999999999')
