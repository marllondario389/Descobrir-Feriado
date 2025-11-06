import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.title("Procurar PDF")
root.geometry("500x500")

# Função de Busca
def buscar ():
    file_path_string = filedialog.askopenfilename()

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# Textos do formulário
canvas.create_text(250, 40, text="Buscar Arquivo PDF", font=("Helvetica", 23, "bold"), fill="blue")

# Botão de Busca
botao_buscar = tk.Button(root, text="Buscar", command=buscar)
canvas.create_window(250, 150, window=botao_buscar,  width = 100, height = 50)


# Loop principal
root.mainloop()