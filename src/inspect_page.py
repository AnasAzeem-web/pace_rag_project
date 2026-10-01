import fitz
import pdfplumber

PDF_PATH = "data/raw/IS456.pdf"

PAGE_NUMBER = 4


print("=" * 100)
print(f"INSPECTING PAGE {PAGE_NUMBER}")
print("=" * 100)


# ---------------------------------------------------------
# PyMuPDF
# ---------------------------------------------------------

with fitz.open(PDF_PATH) as doc:

    page = doc[PAGE_NUMBER - 1]

    print("\nPAGE SIZE")
    print(page.rect.width, "x", page.rect.height)

    print("\nTEXT")
    print("-" * 100)
    print(page.get_text("text", sort=True))

    print("\nBLOCKS")
    print("-" * 100)

    for block in page.get_text("blocks", sort=True):

        x0, y0, x1, y1, text, block_no, block_type = block

        print(
            f"\nBBOX: ({x0:.2f}, {y0:.2f}, {x1:.2f}, {y1:.2f})"
        )
        print(f"TYPE: {block_type}")
        print(f"TEXT: {text.strip()}")


# ---------------------------------------------------------
# pdfplumber
# ---------------------------------------------------------

with pdfplumber.open(PDF_PATH) as pdf:

    page = pdf.pages[PAGE_NUMBER - 1]

    print("\n\n" + "=" * 100)
    print("PDFPLUMBER TABLE DETECTION")
    print("=" * 100)

    tables = page.find_tables()

    print("\nTABLES FOUND:", len(tables))

    for table_number, table in enumerate(tables, start=1):

        print("\n" + "-" * 100)
        print("TABLE:", table_number)
        print("BBOX:", table.bbox)

        print("\nCELLS:")
        for cell in table.cells:
            print(cell)

        print("\nEXTRACTED CONTENT:")
        for row in table.extract():
            print(row)