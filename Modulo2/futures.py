"""
Los Futures en python son como las promesas en javascript
Es una funcion que espera a que otra haga su ejecucion
para despues ejecutarse
"""

import time
# Importamos la libreria Future
from concurrent.futures import Future


"""Aqui lo que hago es crear la funcion que va a ejecutarse
despues de terminar el futuro, y se lo paso por parametro
para hacer alguna tarea deseada con ese resultado
"""
def callback_future(future):
    print("Esto se ejecuta cuando llegue al futuro")
    print(f"Valor seteado al futuro: {future.result()}")


if __name__ == "__main__":
    future = Future()
    """Primero creamos un futuro y le agregamos el done callback
    que su funcion es ejecutar otra funcion al terminar y obtener un resultado
    """
    future.add_done_callback(callback_future)

    print("Iniciando...")

    time.sleep(2)

    print("Terminando...")
    print("Llegamos al futuro")

    """Aqui asignamos ese resultado de alguna ejecucion terminada
    al futuro para despues pasarlo al callback
    """
    future.set_result("Cabimas")