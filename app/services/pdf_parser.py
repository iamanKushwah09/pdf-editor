import fitz

def extract_text_blocks(page: fitz.Page):
    texts = []

    blocks = page.get_text("dict")["blocks"]

    for block in blocks:
        if block["type"] == 0:  # text block
            for line in block["lines"]:
                for span in line["spans"]:
                    if not span["text"].strip():
                        continue

                    x0, y0, x1, y1 = span["bbox"]

                    texts.append({
                        "text": span["text"],
                        "bbox": {
                            "x": x0,
                            "y": y0,
                            "width": x1 - x0,
                            "height": y1 - y0
                        },
                        "font_size": span["size"]
                    })

    return texts
