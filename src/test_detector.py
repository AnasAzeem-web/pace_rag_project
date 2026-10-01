from ingestion.pdf_detector import detect_pdf_pages


PDF_PATH = "data/raw/IS456.pdf"


pages = detect_pdf_pages(PDF_PATH)

for page in pages:
    print(page)