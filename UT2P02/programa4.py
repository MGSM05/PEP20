""" Escribe un programa  que lea por teclado un número real entre 1 y 10, simulando una 
    nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en 
    cuenta los siguientes rangos:
        • Insuficiente: [0, 5)
        • Suficiente: [5, 6)
        • Bien: [6, 7)
        • Notable: [7, 9)
        • Sobresaliente: [9, 10]
    Si el número introducido no está en ninguno de los rangos anteriores debe mostrar un 
    mensaje de error indicando que la nota no es válida.
    Hay que usar la estructura match."""

nota = float(input("Introduce una nota entre 0 y 10: "))

match nota:
    case n if 0 <= n < 5:
        print("Insuficiente")
    case n if 5 <= n < 6:
        print("Suficiente")
    case n if 6 <= n < 7:
        print("Bien")
    case n if 7 <= n < 9:
        print("Notable")
    case n if 9 <= n <= 10:
        print("Sobresaliente")
    case _:
        print("Error: la nota no es válida.")