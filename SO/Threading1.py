import threading

def trabalhador(num):
    
    while True:
        ativas = threading.active_count()-1
        print(f"Trabalhador: {num} de {ativas} threads ativas")

for i in range(5):
    t = threading.Thread(target=trabalhador, args=(i,))
    t.start()