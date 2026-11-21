from app.draft import ResumeDraft
from app.services.guided import apply_answer, guided_turn


def test_invalid_email_is_rejected():
    d = ResumeDraft(name='A')
    assert apply_answer(d, 'email', 'nope') is not None
    assert d.email is None


def test_education_is_parsed():
    d = ResumeDraft()
    assert apply_answer(d, 'education', 'B.Tech CSE, SRM IST, 2022-2026, 8.5') is None
    assert d.education[0].institution == 'SRM IST'
    assert d.education[0].cgpa == '8.5'


def test_first_turn_asks_for_name():
    assert 'name' in guided_turn(ResumeDraft(), None).lower()
