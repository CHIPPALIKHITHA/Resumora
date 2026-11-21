from io import BytesIO

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt

from app.schema import Resume

FONT = 'Calibri'


def _new_document() -> Document:
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Mm(210)
    sec.page_height = Mm(297)
    sec.left_margin = sec.right_margin = Mm(18)
    sec.top_margin = sec.bottom_margin = Mm(15)
    normal = doc.styles['Normal']
    normal.font.name = FONT
    normal.font.size = Pt(10.5)
    normal.element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
    normal.paragraph_format.space_after = Pt(0)
    return doc


def _run(paragraph, text, bold=False, size=None):
    run = paragraph.add_run(text)
    run.bold = bold
    if size:
        run.font.size = Pt(size)
    return run


def header(doc, r: Resume):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _run(p, r.name, bold=True, size=18)
    parts = [r.email, r.phone]
    if r.linkedin:
        parts.append(r.linkedin)
    if r.github:
        parts.append(r.github)
    c = doc.add_paragraph()
    c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _run(c, ' | '.join(parts), size=9.5)


def _heading(doc, title: str):
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    borders = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    for key, value in (('w:val', 'single'), ('w:sz', '6'), ('w:space', '1'), ('w:color', '000000')):
        bottom.set(qn(key), value)
    borders.append(bottom)
    pPr.append(borders)
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    _run(p, title.upper(), bold=True, size=11)


def summary_section(doc, r: Resume):
    if not r.summary:
        return
    _heading(doc, 'Summary')
    doc.add_paragraph(r.summary)


def education_section(doc, r: Resume):
    if not r.education:
        return
    _heading(doc, 'Education')
    for e in r.education:
        p = doc.add_paragraph()
        _run(p, f'{e.degree}, {e.institution}', bold=True)
        detail = f'{e.start} - {e.end}'
        if e.cgpa:
            detail += f' | CGPA: {e.cgpa}'
        doc.add_paragraph(detail)


def _bullets(doc, items):
    for b in items:
        doc.add_paragraph(b, style='List Bullet')


def experience_section(doc, r: Resume):
    if not r.experience:
        return
    _heading(doc, 'Experience')
    for e in r.experience:
        p = doc.add_paragraph()
        _run(p, f'{e.role}, {e.company}', bold=True)
        doc.add_paragraph(f'{e.start} - {e.end}')
        _bullets(doc, e.bullets)


def projects_section(doc, r: Resume):
    if not r.projects:
        return
    _heading(doc, 'Projects')
    for pr in r.projects:
        title = pr.name
        if pr.tech:
            title += ' | ' + ', '.join(pr.tech)
        p = doc.add_paragraph()
        _run(p, title, bold=True)
        _bullets(doc, pr.bullets)
        if pr.link:
            doc.add_paragraph(pr.link)
