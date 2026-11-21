import pytest
from pydantic import ValidationError

from app.schema import Resume


def test_minimal_resume_is_valid():
    r = Resume(name='A B', email='a@b.com', phone='9999999999')
    assert r.skills == []
