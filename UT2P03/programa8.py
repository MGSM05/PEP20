"""Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación 
    solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va 
    respondiendo si el número a adivinar es mayor o menor que el introducido. El programa 
    termina cuando se acierta el número.
    Puedes generar el número usando la función random.randrange(1, 21) para 
    obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio 
    del programa).
    Mejora el programa de forma que el usuario tenga solo 3 intentos."""

import random

numero_secreto = random.randrange(1, 21)
intentos = 3

for i in range(1, intentos + 1):
    intento = int(input(f"\nIntento {i}: Introduce un numero del 1 al 20 : "))

    if intento == numero_secreto:
        print(f"Has ACERTADO el numero secreto que es {numero_secreto} en {i} intento(s).")
        break
    elif intento < numero_secreto:
        print("El numero secreto es MAYOR.")
    else:
        print("El numero secreto es MENOR.")

    if i == intentos:
        print(f"Has agotado tus intentos. El numero era {numero_secreto}.")