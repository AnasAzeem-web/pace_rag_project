from ingestion.text_extractor import extract_text_from_pdf


PDF_PATH = "data/raw/IS456.pdf"


pages = extract_text_from_pdf(PDF_PATH)

for page in pages[:3]:
    print("\n" + "=" * 80)
    print("PAGE:", page["page_number"])
    print("=" * 80)
    print(page["text"])