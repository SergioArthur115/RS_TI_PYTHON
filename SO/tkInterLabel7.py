import tkinter as tk
import datetime


class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.frame = tk.Frame(self.nossaTela)
        self.frame.pack()
        r1 = tk.Radiobutton(self.frame, text='Python')
        r1.pack(side=tk.LEFT)
        r2 = tk.Radiobutton(self.frame, text='Java')
        r2.pack(side=tk.LEFT)
        r3 = tk.Radiobutton(self.frame, text='C++')
        r3.pack(side=tk.LEFT)


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
