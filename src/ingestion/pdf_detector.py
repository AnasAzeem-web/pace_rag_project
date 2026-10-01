import pdfplumber


MIN_TEXT_LENGTH = 50


def detect_page_type(page):
    """
    Classify a PDF page based on the amount of selectable text.

    Returns:
        "text"    -> page contains meaningful selectable text
        "scanned" -> page contains little or no selectable text
    """

    text = page.extract_text() or ""

    if len(text.strip()) >= MIN_TEXT_LENGTH:
        return "text"

    return "scanned"


def detect_pdf_pages(pdf_path):
    """
    Detect the type of every page in a PDF.
    """

    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages, start=1):

            page_type = detect_page_type(page)

            pages.append({
                "page_number": page_number,
                "type": page_type
            })

    return pages