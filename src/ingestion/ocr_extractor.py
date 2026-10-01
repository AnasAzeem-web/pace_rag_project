import fitz
import pytesseract
from PIL import Image
import io


def ocr_page(pdf_path, page_number):
    """
    Extract text from one PDF page using OCR.
    """

    document = fitz.open(pdf_path)

    page = document[page_number - 1]

    matrix = fitz.Matrix(2, 2)

    pixmap = page.get_pixmap(
        matrix=matrix,
        alpha=False
    )

    image_bytes = pixmap.tobytes("png")

    image = Image.open(io.BytesIO(image_bytes))

    text = pytesseract.image_to_string(
        image,
        config="--psm 6"
    )

    document.close()

    return text