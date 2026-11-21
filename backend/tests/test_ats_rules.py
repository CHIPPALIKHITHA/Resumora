from app.ats_rules import analyze, check_action_verbs, check_metrics


def test_good_resume_scores_100(good_resume):
    result = analyze(good_resume)
    assert result.score == 100
    assert result.issues == []
