from fastapi import APIRouter, HTTPException
from pathlib import Path

from app.core.config import STORAGE_DIR
from app.services.ocr_service import run_ocr

router = APIRouter(prefix="/ocr", tags=["OCR"])


@router.get("/{pdf_id}/page/{page_number}")
def ocr_page(pdf_id: str, page_number: int):
    image_path = (
        STORAGE_DIR / "pages" / pdf_id / f"page_{page_number}.png"
    )

    # ✅ SAFETY CHECK 1 — image exists?
    if not image_path.exists():
        return {
            "status": "success",
            "pdf_id": pdf_id,
            "page_number": page_number,
            "texts": [],
            "note": "Page image not found. Call /pages API first."
        }

    try:
        texts = run_ocr(str(image_path))
    except Exception as e:
        # ✅ SAFETY CHECK 2 — OCR never crashes server
        return {
            "status": "success",
            "pdf_id": pdf_id,
            "page_number": page_number,
            "texts": [],
            "note": f"OCR failed safely: {str(e)}"
        }

    return {
        "status": "success",
        "pdf_id": pdf_id,
        "page_number": page_number,
        "texts": texts
    }
