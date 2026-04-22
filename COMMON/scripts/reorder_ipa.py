import win32com.client
import pythoncom
import re
from pathlib import Path

pythoncom.CoInitialize()

def extract_questions(text):
    pattern = r'(\d+)\.?\s*(.+?)\s*\n?\s*([a-d])\.\s*(.+?)\s*\n?\s*([a-d])\.\s*(.+?)\s*\n?\s*([a-d])\.\s*(.+?)\s*\n?\s*([a-d])\.\s*(.+?)(?=\d+\.|\Z)'
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

try:
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True
    
    doc = word.Documents.Open(r"C:\Users\Admin\Desktop\New folder (2)\IPA 6.docx")
    
    full_text = ""
    for para in doc.Paragraphs:
        full_text += para.Range.Text
    
    doc.Close(False)
    
    new_doc = word.Documents.Add()
    
    # Kop
    kop = new_doc.Content
    kop.Text = "Soal Ujian Sekolah Ilmu Pengetahuan Alam\tT.P. 2025/2026\n\nPilihan Berganda (50%)\n\n"
    
    # Parse and reorder
    lines = full_text.split('\n')
    
    current_q = ""
    options = {}
    output_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        m = re.match(r'^(\d+)\.\s*(.*)', line)
        if m:
            if current_q and options:
                output_lines.append(current_q)
                for opt in ['a', 'b', 'c', 'd']:
                    if opt in options:
                        output_lines.append(f"{opt}. {options[opt]}")
                output_lines.append("")
            
            num = m.group(1)
            q_text = m.group(2)
            current_q = f"{num}. {q_text}"
            options = {}
        else:
            m = re.match(r'^([a-d])\.\s*(.*)', line, re.I)
            if m:
                opt_key = m.group(1).lower()
                opt_text = m.group(2)
                options[opt_key] = opt_text
    
    if current_q and options:
        output_lines.append(current_q)
        for opt in ['a', 'b', 'c', 'd']:
            if opt in options:
                output_lines.append(f"{opt}. {options[opt]}")
    
    for line in output_lines:
        new_doc.Content.InsertAfter(line + "\n")
    
    new_doc.SaveAs(r"C:\Users\Admin\Desktop\New folder (2)\IPA_Reorder.docx")
    new_doc.Close()
    word.Quit()
    
    print("DONE! File saved: IPA_Reorder.docx")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

pythoncom.CoUninitialize()