from pathlib import Path
import fitz
from app.core.config import STORAGE_DIR

PAGES_DIR = STORAGE_DIR / "pages"
PAGES_DIR.mkdir(parents=True, exist_ok=True)

def render_page_image(doc: fitz.Document, page_number: int, pdf_id: str, dpi: int = 150):
    page = doc.load_page(page_number)
    pix = page.get_pixmap(dpi=dpi)

    page_dir = PAGES_DIR / pdf_id
    page_dir.mkdir(parents=True, exist_ok=True)

    image_path = page_dir / f"page_{page_number + 1}.png"
    pix.save(image_path)

    return {
        "path": str(image_path),
        "width": pix.width,
        "height": pix.height,
        "dpi": dpi
    }
