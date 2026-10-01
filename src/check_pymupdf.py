import fitz

doc = fitz.open("data/raw/IS456.pdf")

for i in [1, 2, 17, 18, 19]:
    text = doc[i].get_text("text").strip()
    print(f"Page {i + 1}: {len(text)} characters")