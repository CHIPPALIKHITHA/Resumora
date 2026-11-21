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
