import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2, requests, re
from datetime import datetime

#Integrantes Alunos do Projeto:
#Alex de Albuquerque - 202402720805 / Marllon Blenny - 202402368834 / Caio Da Silva Maciel - 202403494272

root = tk.Tk()
root.title("Procurar PDF")
root.geometry("500x500")

# Função para Ler PDF 
def Get_text_from_PDFfiles_usingPyPDF2():
    file_path_string = filedialog.askopenfilename(filetypes=[("PDF","*.pdf")])
    if not file_path_string:
        return
    reader = PyPDF2.PdfReader(file_path_string)
   
    first_page_text = reader.pages[0].extract_text()
    print(first_page_text)
   
    txt = first_page_text or ""
    for p in reader.pages[1:]:
        txt += "\n" + (p.extract_text() or "")

    # extrair datas 
    found = set()
    for s in re.findall(r"\b(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{1,2}-\d{1,2})\b", txt):
        for fmt in ("%d/%m/%Y","%Y-%m-%d"):
            try:
                found.add(datetime.strptime(s,fmt).date())
                break
            except:
                pass

    payload = {}
    headers = {
      'accept': 'application/json',
      'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
    }

    byyear = {}
    for y in sorted({d.year for d in found}):
        url = f"https://date.nager.at/api/v3/PublicHolidays/{y}/BR"
        try:
            response = requests.request("GET", url, headers=headers, data=payload, timeout=8)
            js = response.json()
            byyear[y] = {datetime.strptime(h["date"],"%Y-%m-%d").date():h for h in js}
        except:
            byyear[y] = {}

    out = []
    for d in sorted(found):
        h = byyear.get(d.year, {})
        if d in h:
            out.append(f"{d.isoformat()} — FERIADO: {h[d].get('localName','')}")
        else:
            out.append(f"{d.isoformat()} — NÃO é feriado")

    resultado_text.config(state="normal")
    resultado_text.delete("1.0","end")
    resultado_text.insert("1.0","\n".join(out))
    resultado_text.config(state="disabled")

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# Titulo do Painel
canvas.create_text(250, 40, text="Buscar Arquivo PDF", font=("Helvetica", 23, "bold"), fill="blue")

# Botão de Busca 
botao_buscar = tk.Button(root, text="Buscar", command=Get_text_from_PDFfiles_usingPyPDF2)
canvas.create_window(250, 150, window=botao_buscar, width=100, height=50)

# Resultado dos Feriados 
resultado_text = tk.Text(root, height=15, width=40, state="disabled")
canvas.create_window(250, 320, window=resultado_text, anchor="center")

root.mainloop()
