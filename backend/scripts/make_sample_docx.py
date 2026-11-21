from pathlib import Path

from app.sample_data import SAMPLE_RESUME
from app.services.docx_builder import build_docx

out = Path('out')
out.mkdir(exist_ok=True)
(out / 'sample.docx').write_bytes(build_docx(SAMPLE_RESUME))
print('Wrote out/sample.docx')
