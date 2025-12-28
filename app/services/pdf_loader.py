import fitz
from app.core.config import UPLOAD_DIR

def load_pdf(pdf_id: str):
    pdf_path = UPLOAD_DIR / f"{pdf_id}.pdf"

    if not pdf_path.exists():
        raise FileNotFoundError("PDF not found")

    return fitz.open(pdf_path)
