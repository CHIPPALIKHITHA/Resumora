import re

from fastapi import APIRouter
from fastapi.responses import Response

from app.schema import Resume
from app.services.docx_builder import build_docx
from app.services.pdf_builder import build_pdf

router = APIRouter(prefix='/export')

DOCX_TYPE = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'


def _filename(name: str, ext: str) -> str:
    safe = re.sub(r'[^A-Za-z0-9_-]', '', name.replace(' ', '_')) or 'Resume'
    return f'{safe}_Resume.{ext}'


@router.post('/pdf')
def export_pdf(resume: Resume):
    data = build_pdf(resume)
    headers = {'Content-Disposition': f'attachment; filename="{_filename(resume.name, "pdf")}"'}
    return Response(content=data, media_type='application/pdf', headers=headers)


@router.post('/docx')
def export_docx(resume: Resume):
    data = build_docx(resume)
    headers = {'Content-Disposition': f'attachment; filename="{_filename(resume.name, "docx")}"'}
    return Response(content=data, media_type=DOCX_TYPE, headers=headers)
