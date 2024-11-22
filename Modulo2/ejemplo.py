"""
Ejemplo practico tomando datos de una api
"""

import threading
import queue
import requests
import time

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def fetch_pokemon(pokemon_name, pokemon_queue):
    try:
        response = requests.get(f"{BASE_URL}{pokemon_name}")
        pokemon_data= response.json()
        pokemon_queue.put(pokemon_data)
    
    except Exception as e:
        print(f"error: {e}")


def main():
    pokemon_list = [
        "bulbasaur",
        "ivysaur",
        "venusaur",
        "charmander",
        "pikachu",
        "charizard"
    ]

    pokemon_queue = queue.Queue()

    threads_list = []
    for name in pokemon_list:
        thread = threading.Thread(target=fetch_pokemon, args=(name, pokemon_queue))
        thread.start()
        threads_list.append(thread)

    for thread in threads_list:
        thread.join()

    while not pokemon_queue.empty():
        result = pokemon_queue.get()
        print(f"Nombre del pokemon: {result['name']}")
        print(f"id: {result['id']}")
        print("=" * 20)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Tiempo de ejecucion: {end_time - start_time} segundos")