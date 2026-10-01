import pdfplumber

from ingestion.table_extractor import extract_tables_from_page


PDF_PATH = "data/raw/IS456.pdf"


with pdfplumber.open(PDF_PATH) as pdf:

    for page_number, page in enumerate(pdf.pages, start=1):

        tables = extract_tables_from_page(page)

        if not tables:
            continue

        print("\n" + "=" * 100)
        print("PAGE:", page_number)
        print("TABLES FOUND:", len(tables))
        print("=" * 100)

        for table in tables:

            print("\nTABLE:", table["table_number"])
            print("BBOX:", table["bbox"])

            for row in table["cells"]:
                print(row)