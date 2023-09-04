import tkinter as tk


class Tela:
    def __init__(self, master):
        self.nossaTela = master

        self.frame = tk.Frame(self.nossaTela)
        self.frame.pack(ipadx=30, ipady=30)

        self.lb1 = tk.Label(self.frame, text="Insira os segundos: ")
        self.lb1.pack(side=tk.LEFT)

        self.entrada = tk.Entry(self.frame)
        self.entrada.pack(side=tk.LEFT, padx=20)

        self.btn = tk.Button(self.nossaTela, text="Converter",
                             bg='red', command=self.conversor)
        self.btn.pack()

        self.saida = tk.Label(self.nossaTela, font=('Arial', 16))
        self.saida.pack(pady=15)

    def conversor(self):
        segundos = int(self.entrada.get())
        hs = str(segundos//3600)
        min = str((segundos % 3600)//60)
        seg = str((segundos % 3600) % 60)
        conversao = "{} Horas {} Minutos {} Segundos".format(hs, min, seg)
        self.saida['text'] = conversao


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
