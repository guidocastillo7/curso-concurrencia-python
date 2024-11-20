"""
Deadlock es cuando un grupo de threads
se esperan unos a otros y ninguno puede continuar
No es que hay una solucion de codigo para esto
simplemente tengo que saber organizar los threads
para que esto no me pase
"""

import threading
import time

recurso_1 = threading.Lock()
recurso_2 = threading.Lock()


"""
Aqui lo que hago es cruzar los 2 recursos
el recurso 1 espera al 2 y viceversa
por lo tanto se crea un deadlock
y asi nunca termina de ejecutarse el programa
"""
def proceso_1():
    with recurso_1:
        print("Proceso 1 tiene recurso 1")
        time.sleep(1)
        print("Proceso 1 esperando por recurso 2")
        with recurso_2:
            print("Proceso 1 tiene recurso 2")


def proceso_2():
    with recurso_2:
        print("Proceso 2 tiene recurso 2")
        time.sleep(1)
        print("Proceso 2 esperando por recurso 1")
        with recurso_1:
            print("Proceso 2 tiene recurso 1")
"""
Entonces aqui la solucion es simplemente
revisar mi codigo y ver donde estoy haciendo ese cruce
corregirlo y organizar bien el flujo de los threads
"""


thread_1 = threading.Thread(target=proceso_1)
thread_2 = threading.Thread(target=proceso_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()