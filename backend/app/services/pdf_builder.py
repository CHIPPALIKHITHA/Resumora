from io import BytesIO
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

from app.schema import Resume
from app.services import pdf_styles as S


def _p(text, style):
    return Paragraph(escape(text), style)


def _section_heading(title):
    return [
        Paragraph(title.upper(), S.HEADING),
        HRFlowable(width='100%', thickness=0.6, color=colors.black, spaceAfter=3),
    ]


def header(r: Resume):
    parts = [r.email, r.phone]
    if r.linkedin:
        parts.append(r.linkedin)
    if r.github:
        parts.append(r.github)
    return [_p(r.name, S.NAME), _p(' | '.join(parts), S.CONTACT)]


def summary_section(r: Resume):
    if not r.summary:
        return []
    return [*_section_heading('Summary'), _p(r.summary, S.BODY)]


def education_section(r: Resume):
    if not r.education:
        return []
    out = list(_section_heading('Education'))
    for e in r.education:
        out.append(_p(f'{e.degree}, {e.institution}', S.BOLD))
        detail = f'{e.start} - {e.end}'
        if e.cgpa:
            detail += f' | CGPA: {e.cgpa}'
        out.append(_p(detail, S.BODY))
        out.append(Spacer(1, 3))
    return out


def projects_section(r: Resume):
    if not r.projects:
        return []
    out = list(_section_heading('Projects'))
    for p in r.projects:
        title = p.name
        if p.tech:
            title += ' | ' + ', '.join(p.tech)
        out.append(_p(title, S.BOLD))
        out.extend(_bullets(p.bullets))
        if p.link:
            out.append(_p(p.link, S.BODY))
        out.append(Spacer(1, 3))
    return out


def skills_section(r: Resume):
    if not r.skills:
        return []
    return [*_section_heading('Skills'), _p(', '.join(r.skills), S.BODY)]
