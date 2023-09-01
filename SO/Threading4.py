from threading import Thread, Lock, Condition
import time
import random

armazem = []
#trava = Lock()
trava = Condition()
tam_arm = 10


class ProdutorThread(Thread):
    def run(self):
        global armazem

        while True:
            trava.acquire()
            if len(armazem) < tam_arm:
                print("Armazem cheio, Produtor vai dormir")
                trava.wait()
                print("Há espaço no armazém: Produtor avisado")
            armazem.append(random.randrange(0, 9))
            print(f"Produzido {armazem[-1]}")
            print(f"Lista do produtor{armazem} \n")
            trava.notify()
            trava.release()
            time.sleep(random.random())


class ConsumidorThread(Thread):
    def run(self):
        global armazem

        while True:
            trava.acquire()
            if not armazem:
                print("Nada no armazém, consumidor vai dormir")
                trava.wait()
                print("Produtor adicionou no armazém e avisou ao consumidor")
            num = armazem.pop(0)
            print(f"Consumiu {num}")
            print(f"Lista do Consumidor{armazem} \n")
            trava.notify()
            trava.release()
            time.sleep(random.random())


if __name__ == "__main__":
    ProdutorThread().start()
    ConsumidorThread().start()
