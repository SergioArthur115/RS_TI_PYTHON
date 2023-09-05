import tkinter as tk


class Tela:

    def __init__(self, master):
        self.nossaTela = master

        self.frame = tk.Frame(self.nossaTela)
        self.frame.pack(ipadx=30, ipady=30)

        self.lb1 = tk.Label(self.frame, text="Informe o nome: ")
        self.lb1.pack(side=tk.LEFT)

        self.entrada1 = tk.Entry(self.frame)
        self.entrada1.pack(side=tk.LEFT, padx=20)

        self.frame2 = tk.Frame(self.nossaTela)
        self.frame2.pack(ipadx=30, ipady=30)

        self.lb2 = tk.Label(self.frame2, text="Informe o telefone: ")
        self.lb2.pack(side=tk.LEFT)

        self.entrada2 = tk.Entry(self.frame2)
        self.entrada2.pack(side=tk.LEFT, padx=20)

        self.btn = tk.Button(self.nossaTela, text="Cadastrar", bg='red',command=self.cadastrar)
        self.btn.pack()

        self.saida = tk.Label(self.nossaTela, font=('Arial', 16))
        self.saida.pack(pady=15)
    
    def cadastrar(self):
        nome = self.entrada1.get()
        telefone = self.entrada2.get()

        print("Nome: ",nome)
        print("Telefone: ",telefone)


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
