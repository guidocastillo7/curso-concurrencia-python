"""
Los queues son una manera de organizar datos o tareas
que se quieren trabajar con varios hilos
como si metiera los datos en una 'cola'
para ser consumidos de forma ordenada uno tras otro
"""

"""
Hay que saber que existen 2 tipos de queues
FIFO: First in First out (queue.Queue)
LIFO: Last in First out (queue.LifoQueue)
"""

import time
import threading
# Importamos la libreria queue
import queue

# Creamos una funcion para mostrar los datos del queue mientras no este vacio
def show_queue():
    while not new_queue.empty():
        # Con get obtenemos un dato del queue y lo elimina de una vez
        item = new_queue.get()
        print(f"Item: {item}")

        # Con task_done indicamos que se termino de procesar el elemento
        new_queue.task_done()
        time.sleep(1)


if __name__ == "__main__":
    # Creamos el queue FIFO
    new_queue = queue.Queue()

    for valor in range(1, 20):
        # Con put agregamos un elemento al queue
        new_queue.put(valor)

    print("Queue lleno!")
    print(f"\nDatos del queue: {new_queue}")

    # Creamos 4 hilos para que vayan procesando el metodo en paralelo
    for _ in range(4):
        thread = threading.Thread(target=show_queue)
        thread.start()