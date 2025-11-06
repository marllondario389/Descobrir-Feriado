import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import PyPDF2
import requests


root = tk.Tk()
root.title("Procurar PDF")
root.geometry("500x500")


# Função de Busca
def Get_text_from_PDFfiles_usingPyPDF2(): 
    file_path_string = filedialog.askopenfilename()
    reader = PyPDF2.PdfReader(file_path_string) 
    print(reader.pages[0].extract_text())

url = "https://date.nager.at/api/v3/PublicHolidays/2024/BR"

payload = {}
headers = {
  'accept': 'application/json',
  'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
  }

resultado_text = requests.request("GET", url, headers=headers, data=payload)
    
print(resultado_text)
     
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# Textos do formulário
canvas.create_text(250, 40, text="Buscar Arquivo PDF", font=("Helvetica", 23, "bold"), fill="blue")

# Botão de Busca
botao_buscar = tk.Button(root, text="Buscar", command=Get_text_from_PDFfiles_usingPyPDF2)
canvas.create_window(250, 150, window=botao_buscar,  width = 100, height = 50)

# Resultado da busca
resultado_text = tk.Text(root, height=15, width=40)
canvas.create_window(250, 320, window=resultado_text, anchor="center")



# Loop principal
root.mainloop()