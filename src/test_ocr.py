from ingestion.ocr_extractor import ocr_page


PDF_PATH = "data/raw/IS456.pdf"


for page_number in [2, 3]:

    print("\n" + "=" * 80)
    print("PAGE:", page_number)
    print("=" * 80)

    text = ocr_page(PDF_PATH, page_number)

    print(text)