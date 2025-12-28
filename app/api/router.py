from fastapi import APIRouter

from app.api.v1.pdf_routes import router as pdf_router
from app.api.v1.ocr_routes import router as ocr_router

api_router = APIRouter()

api_router.include_router(pdf_router)
api_router.include_router(ocr_router)
