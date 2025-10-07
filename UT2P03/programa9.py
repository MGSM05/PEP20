""" Escribe un programa para jugar a una versión muy simplificada del black jack. En primer 
    lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A 
    continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando 
    para obtener su puntuación,  hasta que el quiera. Si se pasa de 21 pierde, si obtiene una 
    puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la 
    banca gana."""
import random

banca = random.randint(17, 21)
print("La banca ha sacado sus cartas (la puntuación se revelará al final)")

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