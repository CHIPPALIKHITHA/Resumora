from pathlib import Path

from app.sample_data import SAMPLE_RESUME
from app.services.pdf_builder import build_pdf

out = Path('out')
out.mkdir(exist_ok=True)
(out / 'sample.pdf').write_bytes(build_pdf(SAMPLE_RESUME))
print('Wrote out/sample.pdf')
