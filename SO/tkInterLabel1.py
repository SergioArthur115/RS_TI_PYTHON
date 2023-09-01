import tkinter as tk


class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.l1 = tk.Label(self.nossaTela, text="label 1", font=('Arial', 16))
        self.l1.pack()
        self.l2 = tk.Label(self.nossaTela, text="label 2", font=('Arial', 16))
        self.l2.pack(side=tk.BOTTOM)
        self.l3 = tk.Label(self.nossaTela, text="label 3", font=('Arial', 16))
        self.l3.pack(side=tk.LEFT)
        self.l4 = tk.Label(self.nossaTela, text="label 4", font=('Arial', 16))
        self.l4.pack(side=tk.RIGHT)


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
