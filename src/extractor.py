import fitz  # pymupdf
import re
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]

        # 1. Try direct text extraction
        text = page.get_text()
        if text.strip():
            full_text += text + "\n"
            continue
        
        # 2. If no text, fallback to OCR
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        ocr_text = pytesseract.image_to_string(img)
        full_text += ocr_text + "\n"

    # Clean text
    full_text = re.sub(r"\s+", " ", full_text)
    return full_text
