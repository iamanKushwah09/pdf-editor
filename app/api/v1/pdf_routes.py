from fastapi import APIRouter, UploadFile, File, HTTPException

from app.utils.file_utils import validate_pdf, save_pdf
from app.services.pdf_renderer import get_pdf_pages_data
from app.models.edit_models import ExportRequest
from app.services.pdf_exporter import export_pdf

router = APIRouter(prefix="/pdf", tags=["PDF"])

# =========================
# 1️⃣ UPLOAD PDF
# =========================
@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    validate_pdf(file)
    pdf_id = save_pdf(file)
    return {
        "status": "success",
        "pdf_id": pdf_id
    }

# =========================
# 2️⃣ GET PAGES + TEXT
# =========================
@router.get("/{pdf_id}/pages")
def get_pdf_pages(pdf_id: str):
    try:
        pages = get_pdf_pages_data(pdf_id)
        return {
            "status": "success",
            "pdf_id": pdf_id,
            "pages": pages
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="PDF not found")

# =========================
# 3️⃣ EXPORT EDITED PDF
# =========================
@router.post("/{pdf_id}/export")
def export_edited_pdf(pdf_id: str, payload: ExportRequest):
    try:
        output_path = export_pdf(pdf_id, payload.edits)
        return {
            "status": "success",
            "pdf_id": pdf_id,
            "output_pdf": output_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
