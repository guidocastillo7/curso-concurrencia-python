"""
El trabajo con Threads (hilos) consiste en hacer que el codigo
ejecute varias funcionalidades al mismo tiempo
sin esperar a que uno termine para empezar otro
"""


import requests
# Importamos la libreria para crear los hilos
import threading

BASE_URL = "https://pokeapi.co/api/v2/"


def get_pokemon(pokemon_id):
    response = requests.get(f"{BASE_URL}pokemon/{pokemon_id}")

    if response.status_code == 200:
        results = response.json().get("forms")
        name = results[0].get("name")

        print(f"{pokemon_id}: {name}")


if __name__ == "__main__":
    for i in range(1,50):

        # Creamos una variable para el trabajo con hilo
        # Usamos la clase Thread y como parametros le pasamos la funcion a ejecutar
        # y los argumentos de dicha funcion se pasan de segundo parametro
        thread = threading.Thread(target=get_pokemon,
                                  args=[i])
        # Se tiene que iniciar el thread
        thread.start()
        #get_pokemon(i)