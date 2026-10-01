import fitz


def extract_page_text(page):
    """
    Extract normal text from a PyMuPDF page.

    sort=True attempts to place text in a more natural
    top-to-bottom, left-to-right order.
    """

    return page.get_text("text", sort=True).strip()


def extract_page_blocks(page):
    """
    Extract text blocks together with their coordinates.
    """

    blocks = page.get_text("blocks", sort=True)

    extracted = []

    for block in blocks:

        x0, y0, x1, y1, text, block_number, block_type = block

        extracted.append({
            "bbox": (x0, y0, x1, y1),
            "text": text.strip(),
            "block_number": block_number,
            "block_type": block_type
        })

    return extracted


def extract_page_words(page):
    """
    Extract individual words and their coordinates.
    """

    words = page.get_text("words", sort=True)

    extracted = []

    for word in words:

        x0, y0, x1, y1, text, block_number, line_number, word_number = word

        extracted.append({
            "bbox": (x0, y0, x1, y1),
            "text": text,
            "block_number": block_number,
            "line_number": line_number,
            "word_number": word_number
        })

    return extracted


def extract_page_structure(page):
    """
    Extract the useful structural information from one page.
    """

    return {
        "width": page.rect.width,
        "height": page.rect.height,
        "text": extract_page_text(page),
        "blocks": extract_page_blocks(page),
        "words": extract_page_words(page)
    }


def extract_pdf_structure(pdf_path):
    """
    Extract structural information from every page.
    """

    pages = []

    with fitz.open(pdf_path) as doc:

        for page_number, page in enumerate(doc, start=1):

            page_data = extract_page_structure(page)

            page_data["page_number"] = page_number

            pages.append(page_data)

    return pages