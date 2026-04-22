import win32com.client
import pythoncom

pythoncom.CoInitialize()

try:
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True
    
    doc = word.Documents.Open(r"C:\Users\Admin\Desktop\New folder (2)\IPA_Reorder.docx")
    
    print(f"Paragraphs count: {doc.Paragraphs.Count}")
    
    for i, para in enumerate(doc.Paragraphs):
        text = para.Range.Text.strip()
        if text:
            print(f"[{i}] {text}")
    
    doc.Close(False)
    word.Quit()

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

pythoncom.CoUninitialize()