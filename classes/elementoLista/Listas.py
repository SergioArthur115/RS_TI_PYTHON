class Lista:
    def __init__(self, lista):
        self.lista = lista

    def imprimirLista(self):
        newLista = []
        for i in self.lista:
            if i not in newLista:
                newLista.append(i)
        return newLista
