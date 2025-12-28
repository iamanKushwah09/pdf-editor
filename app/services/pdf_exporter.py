from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait
from pathlib import Path
import fitz

from app.core.config import STORAGE_DIR
from app.services.pdf_loader import load_pdf

OUTPUT_DIR = STORAGE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def export_pdf(pdf_id: str, edits: list):
    original_pdf_path = STORAGE_DIR / "uploads" / f"{pdf_id}.pdf"
    output_path = OUTPUT_DIR / f"{pdf_id}_edited.pdf"

    doc = fitz.open(original_pdf_path)

    c = canvas.Canvas(str(output_path))

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)

        # 1️⃣ Render page as image
        pix = page.get_pixmap(dpi=150)
        img_path = OUTPUT_DIR / f"{pdf_id}_page_{page_index+1}.png"
        pix.save(img_path)

        width, height = pix.width, pix.height
        c.setPageSize((width, height))
        c.drawImage(str(img_path), 0, 0, width, height)

        # 2️⃣ Apply edited texts for this page
        for edit in edits:
            if edit.page_number == page_index + 1:
                c.setFont("Helvetica", edit.font_size)
                c.drawString(
                    edit.x,
                    height - edit.y,  # PDF coordinate fix
                    edit.text
                )

        c.showPage()

    c.save()
    doc.close()

    return str(output_path)
