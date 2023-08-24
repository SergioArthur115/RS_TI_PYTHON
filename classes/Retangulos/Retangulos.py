class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        return self.largura*self.altura

    def calcularPerimetro(self):
        return 2*(self.largura+self.altura)
