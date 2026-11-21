from app.draft import ResumeDraft, missing_fields


def test_empty_draft_is_missing_everything():
    assert missing_fields(ResumeDraft()) == [
        'name', 'email', 'phone', 'education', 'skills', 'projects', 'summary',
    ]
