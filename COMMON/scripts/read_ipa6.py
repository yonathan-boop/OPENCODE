import win32com.client
import pythoncom
import re
from pathlib import Path

pythoncom.CoInitialize()

try:
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True
    
    doc = word.Documents.Open(r"C:\Users\Admin\Desktop\New folder (2)\IPA 6.docx")
    
    full_text = ""
    for para in doc.Paragraphs:
        full_text += para.Range.Text
    
    print("FILE CONTENT:")
    print("=" * 50)
    print(full_text[:3000])
    print("=" * 50)
    print(f"\nTotal chars: {len(full_text)}")
    
    doc.Close(False)
    word.Quit()
    
except Exception as e:
    print(f"Error: {e}")

pythoncom.CoUninitialize()