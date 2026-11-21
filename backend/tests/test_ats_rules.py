from app.ats_rules import analyze, check_action_verbs, check_metrics


def test_good_resume_scores_100(good_resume):
    result = analyze(good_resume)
    assert result.score == 100
    assert result.issues == []


def test_weak_verb_is_flagged(good_resume):
    r = good_resume.model_copy(deep=True)
    r.projects[0].bullets = ['Worked on a pipeline for air data with 3 sources']
    assert len(check_action_verbs(r)) == 1
