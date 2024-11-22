"""
Los callbacks se usan en la programacion asincrona
Son una funcion que se pasa como argumento a otra funcion
y es llamada despues de alguna operacion especifica
porque tiene que esperar una respuesta especifica para ejecutarse
"""

import requests
import threading


def get_pokemon(response):
    results = response.json().get("forms")
    name = results[0].get("name")
    print(f"Pokemon: {name}")


def error():
    print("No se pudo obtener la información")


"""
En este ejemplo creamos la funcion principal
que va a llevar los callbacks de exito y de error
que van a ser otras funciones que le pasamos por
parametros en el Thread
"""
def get_request(url, success_callback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response)
    else:
        error_callback()


if __name__ == "__main__":
    for i in range(1, 10):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"

        """
        En este caso pasamos los parametros como kwargs
        Por lo tanto tiene que ser en diccionario
        Y las llaves van a ser los nombre de los parametros
        """
        thread = threading.Thread(target=get_request,
                                  kwargs={
                                      "url": url,
                                      "success_callback": get_pokemon,
                                      "error_callback": error
                                  })
        thread.start()