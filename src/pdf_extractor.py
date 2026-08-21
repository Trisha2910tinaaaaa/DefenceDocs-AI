import fitz
from .ocr import ocr_page


def extract_pdf(pdf_path, ocr_threshold=50):

    doc = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(doc, start=1):

        text = page.get_text().strip()

        extraction_method = "text"

        if len(text) < ocr_threshold:
            text = ocr_page(page)
            extraction_method = "ocr"

        pages.append({
            "page_number": page_number,
            "text": text,
            "extraction_method": extraction_method
        })

    return pages