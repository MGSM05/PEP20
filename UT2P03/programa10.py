""" Modifica el programa anterior par que pida en primer lugar el número de jugadores que 
    van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la 
    banca. """

import random

banca = random.randint(17, 21)
print("La banca ha sacado sus cartas (la puntuación se revelará al final)")

num_jugadores = int(input("\nCuantos jugadores van a jugar?: "))

for j in range(1, num_jugadores + 1):
    print(f"\nTurno del jugador {j}")
    jugador = 0

    while True:
        print(f"\nTu puntuación actual es: {jugador}")
        opcion = input("Quieres sacar una carta? (s/n): ").lower()

        if opcion == "s":
            carta = random.randint(1, 5) 
            jugador = jugador + carta
            print(f"Has sacado un {carta}. Tu puntuación total ahora es {jugador}.")

            if jugador > 21:
                print("Te HAS PASADO de 21.")
                print(f"La banca tenía {banca}.")
                break
        elif opcion == "n":
            print(f"\nTu puntuación final: {jugador}")
            print(f"Puntuación de la banca: {banca}")

            if jugador > 21:
                print("Te HAS PASADO de 21.")
            elif jugador > banca:
                print("HAS GANADO Tu puntuación es mayor que la banca.")
            elif jugador == banca:
                print("EMPATE pero la banca gana en caso de EMPATE.")
            else:
                print("Tu puntuación es MENOR que la banca, HAS PERDIDO.")
            break
        else:
            print("Opción no válida. Escribe 's' o 'n'.")