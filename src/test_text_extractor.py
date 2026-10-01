import camelot

PDF_PATH = "data/raw/IS456.pdf"
PDF_PAGE = "33"

for flavor in ["lattice", "stream"]:
    print("\n" + "=" * 60)
    print(f"CAMeLOT: {flavor.upper()}")
    print("=" * 60)

    tables = camelot.read_pdf(
        PDF_PATH,
        pages=PDF_PAGE,
        flavor=flavor
    )

    print("Tables found:", tables.n)

    for i, table in enumerate(tables, start=1):
        print(f"\n--- TABLE {i} ---")
        print("Parsing report:", table.parsing_report)
        print(table.df.to_string(index=False, header=False))