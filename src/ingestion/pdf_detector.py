import pdfplumber


def detect_page_type(page):
    """
    Determine whether a PDF page contains
    meaningful selectable text.

    Returns:
        "text"     -> selectable text exists
        "scanned"  -> little or no selectable text
    """

    text = page.extract_text() or ""

    if len(text.strip()) >= 50:
        return "text"

    return "scanned"


def detect_pdf_pages(pdf_path):
    """
    Classify every page in a PDF as either
    text-based or scanned.
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