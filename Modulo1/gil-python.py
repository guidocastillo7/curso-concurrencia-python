"""
Gil de Python: Global Interpreter Lock
Basicamente lo que esto hace es que 
un solo Thread se ejecute a la vez
permite que solo un Thread tome el control del interprete
Es decir, no se van a ejecutar los threads en paralelo
si los intercala entre milisegundos

Esto ayuda a que no se generen tantos Deadlocks ni Livelocks
entre otra cosas...
"""