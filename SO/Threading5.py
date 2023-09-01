from threading import Thread, Lock, Condition
import time
import random

armazem = []
trava = Lock()
dorme_produtor = Condition()
dorme_consumidor = Condition()
# trava = Condition()
tam_arm = 4


class ProdutorThread(Thread):
    def run(self):
        global armazem
        while True:
            trava.acquire()
            dorme_produtor.acquire()
            dorme_consumidor.acquire()
            if len(armazem) < tam_arm:
                armazem.append(random.randrange(0, 9))
                print(f"Produzido {armazem[-1]}")
                print(f"Lista do produtor {armazem} \n ")

                dorme_consumidor.release()
                dorme_produtor.release()
            else:
                print("Armazém cheio, Produtor vai dormir")
                if trava.locked():
                    trava.release()
                dorme_consumidor.notify()
                dorme_consumidor.release()
                dorme_produtor.wait()

            if trava.locked():
                trava.release()
                time.sleep(random.random())


class ConsumidorThread(Thread):
    def run(self):
        global armazem
        while True:
            trava.acquire()
            dorme_produtor.acquire()
            dorme_consumidor.acquire()
            if len(armazem) > 0:
                num = armazem.pop(0)
                print(f"Consumiu {num}")
                print(f"Lista do consumidor {armazem} \n")

                dorme_consumidor.release()
                dorme_produtor.release()
            else:
                print("Armazem vazio: Consumidor irá dormir")

                if trava.locked():
                    trava.release()

                dorme_produtor.notify()
                dorme_produtor.release()
                dorme_consumidor.wait()

            if trava.locked():
                trava.release()
            time.sleep(random.random())


if __name__ == "__main__":
    Produtor1 = ProdutorThread()
    Produtor2 = ProdutorThread()
    Produtor1.start()
    Produtor2.start()

    Consumidor1 = ConsumidorThread()
    Consumidor2 = ConsumidorThread()
    Consumidor1.start()
    Consumidor2.start()
