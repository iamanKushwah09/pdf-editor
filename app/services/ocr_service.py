from paddleocr import PaddleOCR

# Load once (IMPORTANT for performance)
ocr_engine = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)

def run_ocr(image_path: str):
    result = ocr_engine.ocr(image_path, cls=True)

    texts = []

    for line in result[0]:
        bbox, (text, confidence) = line

        x_coords = [p[0] for p in bbox]
        y_coords = [p[1] for p in bbox]

        x = min(x_coords)
        y = min(y_coords)
        width = max(x_coords) - x
        height = max(y_coords) - y

        texts.append({
            "text": text,
            "bbox": {
                "x": x,
                "y": y,
                "width": width,
                "height": height
            },
            "confidence": confidence
        })

    return texts
