import threading
from math import sin
import time


def expo(x):
    global resp_expo
    time.sleep(10)
    resp_expo = x * x
    print('expo')


def mult(x):
    global resp_mult
    time.sleep(15)
    resp_mult = 3 * x
    print('mult')


def seno(x):
    global resp_seno
    time.sleep(20)
    resp_seno = sin(x)
    print('seno')


if __name__ == '__main__':
    x = 5

    thread1 = threading.Thread(target=expo, args=(x,))
    thread2 = threading.Thread(target=mult, args=(x,))
    thread3 = threading.Thread(target=seno, args=(x,))
    thread1.start()
    # thread1.join()
    print(thread1)
    thread2.start()
    # thread2.join()
    thread3.start()
    thread3.join()

    fx = resp_expo + resp_mult + resp_seno
    print('Equação f(x) = x^2 + 3*x + sen(x)')
    print(f'Resultado para x = {x}: {fx}')
