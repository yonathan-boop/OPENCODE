from docx import Document

doc = Document(r"C:\Users\Admin\Desktop\New folder (2)\IPA 6.docx")

for i, p in enumerate(doc.paragraphs):
    text = p.text.strip()
    print(f"[{i}] {text}")