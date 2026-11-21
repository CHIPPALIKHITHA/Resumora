from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle

FONT = 'Helvetica'
FONT_BOLD = 'Helvetica-Bold'

NAME = ParagraphStyle('Name', fontName=FONT_BOLD, fontSize=18, leading=22, alignment=TA_CENTER)
CONTACT = ParagraphStyle('Contact', fontName=FONT, fontSize=9.5, leading=12, alignment=TA_CENTER)
HEADING = ParagraphStyle('Heading', fontName=FONT_BOLD, fontSize=11, leading=14, spaceBefore=8, spaceAfter=2)
BODY = ParagraphStyle('Body', fontName=FONT, fontSize=10, leading=13)
BOLD = ParagraphStyle('Bold', parent=BODY, fontName=FONT_BOLD)
BULLET = ParagraphStyle('Bullet', parent=BODY, leftIndent=12, bulletIndent=2)
