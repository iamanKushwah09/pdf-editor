from app.services.pdf_loader import load_pdf
from app.services.pdf_parser import extract_text_blocks
from app.utils.image_utils import render_page_image

def get_pdf_pages_data(pdf_id: str):
    doc = load_pdf(pdf_id)

    pages_data = []

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)

        image_info = render_page_image(doc, page_index, pdf_id)
        texts = extract_text_blocks(page)

        pages_data.append({
            "page_number": page_index + 1,
            "width": image_info["width"],
            "height": image_info["height"],
            "dpi": image_info["dpi"],
            "image_path": image_info["path"],
            "texts": texts
        })

    doc.close()
    return pages_data
