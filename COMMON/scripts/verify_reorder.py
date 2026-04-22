import win32com.client
import pythoncom

pythoncom.CoInitialize()

try:
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True
    
    doc = word.Documents.Open(r"C:\Users\Admin\Desktop\New folder (2)\IPA_Reorder.docx")
    
    full_text = ""
    for para in doc.Paragraphs:
        full_text += para.Range.Text
    
    print(full_text[:4000])
    
    doc.Close(False)
    word.Quit()

except Exception as e:
    print(f"Error: {e}")

pythoncom.CoUninitialize()