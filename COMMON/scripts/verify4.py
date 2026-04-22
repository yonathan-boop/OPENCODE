from docx import Document

doc = Document(r"C:\Users\Admin\Desktop\New folder (2)\IPA 6.docx")

for i, p in enumerate(doc.paragraphs[:50]):
    text = p.text.strip()
    if text:
        print(f"[{i}] {text}")