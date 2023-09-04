import tkinter as tk


class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.text1 = tk.Label(self.nossaTela, text="Digite seu nome: ")
        self.text1.pack(side=tk.LEFT)
        self.entrada = tk.Entry(self.nossaTela)
        self.entrada.pack(side=tk.LEFT)
        self.btn = tk.Button(self.nossaTela, text="Confirmar",
                             bg="green", command=self.mostrarNome)
        self.btn.pack(side=tk.LEFT, padx=15)

    def mostrarNome(self):
        self.nome = self.entrada.get()
        print("Seja bem vindo " + self.nome)


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
