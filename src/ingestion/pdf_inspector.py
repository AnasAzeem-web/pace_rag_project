import sys
import fitz
import pdfplumber


def inspect_page(pdf_path, page_number):
    """
    Inspect one PDF page at multiple structural levels.

    page_number is 1-based.
    """

    print("=" * 100)
    print("PDF INSPECTION")
    print("=" * 100)

    # ---------------------------------------------------------
    # PyMuPDF inspection
    # ---------------------------------------------------------

    with fitz.open(pdf_path) as doc:

        if page_number < 1 or page_number > len(doc):
            raise ValueError(
                f"Page number must be between 1 and {len(doc)}"
            )

        page = doc[page_number - 1]

        print("\nPAGE INFORMATION")
        print("-" * 100)

        print("Page:", page_number)
        print("Width:", page.rect.width)
        print("Height:", page.rect.height)

        # -----------------------------------------------------
        # Text
        # -----------------------------------------------------

        print("\nTEXT")
        print("-" * 100)

        text = page.get_text("text", sort=True)

        print(text[:5000])

        # -----------------------------------------------------
        # Blocks
        # -----------------------------------------------------

        print("\nBLOCKS")
        print("-" * 100)

        blocks = page.get_text("blocks", sort=True)

        for block_number, block in enumerate(blocks):

            x0, y0, x1, y1, block_text, block_no, block_type = block

            print(
                f"\nBlock {block_number}"
                f"\n  bbox: ({x0:.2f}, {y0:.2f}, {x1:.2f}, {y1:.2f})"
                f"\n  type: {block_type}"
                f"\n  text: {block_text.strip()[:500]}"
            )

        # -----------------------------------------------------
        # Words
        # -----------------------------------------------------

        print("\nWORDS")
        print("-" * 100)

        words = page.get_text("words", sort=True)

        for word in words[:100]:

            x0, y0, x1, y1, text, block_no, line_no, word_no = word

            print(
                f"({x0:.1f}, {y0:.1f}, {x1:.1f}, {y1:.1f}) "
                f"{text!r} "
                f"[block={block_no}, line={line_no}, word={word_no}]"
            )

        # -----------------------------------------------------
        # Detailed font/span information
        # -----------------------------------------------------

        print("\nSPANS / FONT INFORMATION")
        print("-" * 100)

        page_dict = page.get_text("dict", sort=True)

        span_count = 0

        for block in page_dict["blocks"]:

            if block.get("type") != 0:
                continue

            for line in block.get("lines", []):

                for span in line.get("spans", []):

                    print(
                        f"text={span.get('text')!r} "
                        f"font={span.get('font')!r} "
                        f"size={span.get('size')} "
                        f"flags={span.get('flags')} "
                        f"bbox={span.get('bbox')}"
                    )

                    span_count += 1

                    if span_count >= 100:
                        break

                if span_count >= 100:
                    break

            if span_count >= 100:
                break

    # ---------------------------------------------------------
    # pdfplumber table inspection
    # ---------------------------------------------------------

    print("\n" + "=" * 100)
    print("PDFPLUMBER TABLE ANALYSIS")
    print("=" * 100)

    with pdfplumber.open(pdf_path) as pdf:

        page = pdf.pages[page_number - 1]

        print("\nPAGE SIZE")
        print("-" * 100)

        print("Width:", page.width)
        print("Height:", page.height)

        # -----------------------------------------------------
        # Table finder
        # -----------------------------------------------------

        finder = page.debug_tablefinder()

        print("\nTABLE FINDER")
        print("-" * 100)

        print("Edges:", len(finder.edges))
        print("Intersections:", len(finder.intersections))
        print("Cells:", len(finder.cells))
        print("Tables:", len(finder.tables))

        # -----------------------------------------------------
        # Detected tables
        # -----------------------------------------------------

        for table_number, table in enumerate(finder.tables, start=1):

            print("\n" + "-" * 100)
            print("TABLE:", table_number)
            print("BBOX:", table.bbox)
            print("CELLS:", len(table.cells))

            extracted = table.extract()

            print("\nEXTRACTED TABLE CONTENT")

            for row_number, row in enumerate(extracted):

                print(f"ROW {row_number}:")
                print(row)

        # -----------------------------------------------------
        # Individual cell geometry
        # -----------------------------------------------------

        print("\n" + "-" * 100)
        print("CELL GEOMETRY")
        print("-" * 100)

        for cell_number, cell in enumerate(finder.cells[:100]):

            print(
                f"Cell {cell_number}: {cell}"
            )


if __name__ == "__main__":

    if len(sys.argv) != 3:

        print(
            "Usage:\n"
            "python src/ingestion/pdf_inspector.py "
            "data/raw/IS456.pdf PAGE_NUMBER"
        )

        sys.exit(1)

    pdf_path = sys.argv[1]
    page_number = int(sys.argv[2])

    inspect_page(pdf_path, page_number)