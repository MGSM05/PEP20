""" Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer 
    lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle 
    qué opción desea elegir. Por ejemplo:
        1. Piedra
        2. Papel
        3. Tijera
    Seleccione una opción (1, 2 o 3):
    Después de leer la opción seleccionada por el usuario el programa generará un número 
    aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha 
    ganado o ha perdido dependiendo del resultado.
    Ten en cuenta que:
        • La piedra gana a la tijera pero pierde contra el papel.
        • El papel gana a la piedra pero pierde contra la tijera.
        • La tijera gana al papel pero pierde contra la piedra."""
import random

print ("1. PIEDRA")
print ("2. PAPEL")
print ("3. TIJERA")
opcion = int(input("Selecciona una de las tres opciones (1, 2, 3) : "))

match opcion:
    case 1:
        print("Has elegido PIEDRA")
    case 2:
        print("Has elegido PAPEL")
    case 3:
        print("Has elegido TIJERA")
    case _:
        print("OPCION NO ENCONTRADA")

rival = random.randrange(1, 4)

match rival:
    case 1:
        print("El rival ha elegido PIEDRA")
    case 2:
        print("El rival ha elegido PAPEL")
    case 3:
        print("El rival ha elegido TIJERA")

if opcion == rival:
    print("EMPATE TECNICO")
elif (opcion == 1 and rival == 3) or (opcion == 2 and rival == 1) or (opcion == 3 and rival == 2):
    print("HAS GANADO!!!")
else:
    print("PERDISTE :(")