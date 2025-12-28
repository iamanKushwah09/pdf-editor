from pydantic import BaseModel
from typing import List

class TextEdit(BaseModel):
    page_number: int
    text: str
    x: float
    y: float
    font_size: float

class ExportRequest(BaseModel):
    edits: List[TextEdit]
