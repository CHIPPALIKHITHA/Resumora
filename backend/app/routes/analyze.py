from fastapi import APIRouter

from app.ats_rules import AnalysisResult, analyze
from app.schema import Resume

router = APIRouter()


@router.post('/analyze', response_model=AnalysisResult)
def analyze_resume(resume: Resume):
    return analyze(resume)
