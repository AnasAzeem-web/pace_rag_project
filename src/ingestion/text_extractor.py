import pdfplumber


def extract_text_from_pdf(pdf_path):
    """
    Extract selectable text from every page of a PDF.
    """

    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages, start=1):

            text = page.extract_text() or ""

            pages.append({
                "page_number": page_number,
                "text": text
            })

    return pages