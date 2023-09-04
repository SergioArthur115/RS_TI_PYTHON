import tkinter as tk
import datetime


class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.lb1Relogio = tk.Label(
            self.nossaTela, font=('Arial', 18), fg='blue')
        self.lb1Relogio.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        agora = datetime.datetime.now()
        self.lb1Relogio['text'] = agora.strftime('%H:%M:%S')
        self.nossaTela.after(1000, self.alteracao)


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
