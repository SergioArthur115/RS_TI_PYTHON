import tkinter as soma


class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.entrada1 = soma.Entry(self.nossaTela)
        self.entrada1.pack()
        self.entrada2 = soma.Entry(self.nossaTela)
        self.entrada2.pack()

        self.labelClique = soma.Label(
            self.nossaTela, text="Somar", relief="raised")
        self.labelClique.pack()
        self.labelClique.bind('<Button-1>', self.somar)

    def somar(self, event):
        self.inteiro1 = int(self.entrada1.get())
        self.inteiro2 = int(self.entrada2.get())
        print(self.inteiro1 + self.inteiro2)


janelaRaiz = soma.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
