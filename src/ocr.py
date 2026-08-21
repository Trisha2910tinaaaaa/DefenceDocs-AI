import fitz
import pytesseract
from PIL import Image


def ocr_page(page, dpi=200):
    pix = page.get_pixmap(dpi=dpi)

    image = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
        pix.samples
    )

    return pytesseract.image_to_string(image)