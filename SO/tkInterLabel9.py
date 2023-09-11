import tkinter as tk
from tkinter import filedialog


class Tela:

    def __init__(self, master):

        self.nossaTela = master
        self.arquivoAberto = None
        self.criaWidgets()

    def criaWidgets(self):
        self.lb1 = tk.Label(
            self.nossaTela, text="Informe o nome", font=('Arial', 12))
        self.entradaNome = tk.Entry(self.nossaTela, font=('Arial', 12))
        self.lb2 = tk.Label(
            self.nossaTela, text="Informe o telefone", font=('Arial', 12))
        self.entradaTel = tk.Entry(self.nossaTela, font=('Arial', 12))
        self.cadastrar = tk.Button(self.nossaTela,text="Cadastrar", command=self.cadastrar)
        self.lb1.grid(column=0)
        self.entradaNome.grid(row=0,column=1,padx=20)
        self.lb2.grid(row=1,column=0)
        self.entradaTel.grid(row=1,column=1,padx=20)
        self.cadastrar.grid(row=2,column=0,columnspan=2,pady=20)


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
