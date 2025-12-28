import uuid
from pathlib import Path
from fastapi import UploadFile, HTTPException

from app.core.config import UPLOAD_DIR, ALLOWED_EXTENSIONS, MAX_FILE_SIZE_MB


def validate_pdf(file: UploadFile):
    # Check extension
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    # Check file size (FastAPI gives file.file)
    file.file.seek(0, 2)  # move cursor to end
    size_mb = file.file.tell() / (1024 * 1024)
    file.file.seek(0)

    if size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds {MAX_FILE_SIZE_MB} MB limit"
        )


def save_pdf(file: UploadFile) -> str:
    pdf_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{pdf_id}.pdf"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return pdf_id
