"""
El Race Condition es un error comun trabajando con Threads
Es cuando 2 o mas threads deben ejecutarse en un orden correcto
pero el programa no fue configurado para que lo haga en orden
y lo que pasa es que los resultados no son los esperados
siempre varian, mas que todo cuando se comparten variables o algun dato
y siempre da un resultado diferente
"""

import threading

contador = 0

"""
En este caso que sumamos y restamos la misma variable
trabajando con hilos al mismo tiempo
nunca nos da el resultado esperado que es 0
porque no se ejecuta en un orden
"""

"""
Otra solucion es usar un Lock
que bloquea la variable para que ningun otra funcion
la pueda usar hasta que termine su ejecucion
Se tiene que usar en conjunto con join, sino no funciona
"""
# Creamos la variable para el Lock
lock = threading.Lock()


def sumar_contador():
    global contador
    for _ in range(1,1000000):
        # Usamos la suma del contador con el Lock
        # Asi se bloquea hasta que termine de ejecutarse
        with lock:
            contador += 1


def restar_contador():
    global contador
    for _ in range(1,1000000):
        # Hacemos lo mismo con esta funcion
        with lock:
            contador -= 1


thread_sumar = threading.Thread(target=sumar_contador)
thread_restar = threading.Thread(target=restar_contador)

thread_sumar.start()
thread_restar.start()

"""
Una solucion es usar .join()
esto hace que los threads se ejecuten en orden
y uno espere que termine el otro para ejecutarse
pero a veces no es suficiente con eso
"""
thread_sumar.join()
thread_restar.join()

print(f"Valor final del contador {contador}")