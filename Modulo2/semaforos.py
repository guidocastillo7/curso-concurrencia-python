"""
Los Semaforos sirven para controlar el flujo de procesos
funciona literalmente como un semaforo dejando procesar tantos hilos (en este caso)
como sean configurados en cada contador de cada semaforo
Este patrón es útil en escenarios donde es importante que las tareas sigan un orden específico,
incluso si se ejecutan de manera concurrente
"""

import threading

# Creamos los semafotos con su contador en 0, como si esta cerrado
semaforo1 = threading.Semaphore(0)
semaforo2 = threading.Semaphore(0)


def fun_1():
    print(1)
    """Con release aumentamos el contador a 1, que significa
    que lo abre y deja procesar a 1 hilo en este caso
    """
    semaforo1.release()

    """Con acquire restamos el contador 1 valor, que significa
    que lo vuelve a 0 y lo cierra y no deja procesar ningun hilo
    """
    semaforo2.acquire()
    print(3)
    semaforo1.release()


def fun_2():
    semaforo1.acquire()
    print(2)
    semaforo2.release()
    semaforo1.acquire()
    print(4)


# Creamos los dos hilos y los iniciamos de una vez
threading.Thread(target=fun_1).start()
threading.Thread(target=fun_2).start()