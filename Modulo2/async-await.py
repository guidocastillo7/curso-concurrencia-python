"""
Las funciones asincronas son otra forma de concurrencia
porque son funciones que pueden ejecutarse sin esperar
a que otra termine, es decir, podemos hacer varias tareas 
al mismo tiempo y no esperar que una termine para empezar otra
"""

# Importamos la libreria asyncio
import asyncio


# Se crea la funcion asincrona
async def tarea1():
    print("Ejecutando tarea 1..")
    # Con esto se frena 2 segundos
    await asyncio.sleep(2)


# Creamos varias tareas para probar que se ejecutan al mismo tiempo
async def tarea2():
    print("Ejecutando tarea 2..")
    await asyncio.sleep(4)


async def tarea3():
    print("Ejecutando tarea 3..")
    await asyncio.sleep(6)


# Trabajando con funciones asincronas siempre tenemos que crear un metodo main
async def main():
    print("Estamos en el metodo Main")

    """Se crean las tareas con la libreria asyncio
    y se pasa por parametro la funcion
    """
    tarea_1 = asyncio.create_task(tarea1())
    tarea_2 = asyncio.create_task(tarea2())
    tarea_3 = asyncio.create_task(tarea3())

    """Aqui llamamos a que haga las tareas
    y se ejecutan al mismo tiempo, cada una termina en el tiempo
    que necesite mientras las otras se siguen ejecutando
    """
    await tarea_1
    print("Termino la tarea 1 en 2 segundos")
    await tarea_2
    print("Termino la tarea 2 en 4 segundos")
    await tarea_3
    print("Termino la tarea 4 en 6 segundos")

    """Otra manera de ejecutar todas las tareas es usando gather
    se pasan por parametro todas las tareas a ejecutar
    """
    await asyncio.gather(tarea_1, tarea_2, tarea_3)

    # Y la otra manera mas optima es hacerlo con un list comprehension
    tasks_list= [tarea1, tarea2, tarea3]
    async_tasks = [asyncio.create_task(task()) for task in tasks_list]
    await asyncio.gather(*async_tasks)

    print("\nTerminamos todas las tareas.")


# Ejecutamos el main para que inicie las tareas
asyncio.run(main())