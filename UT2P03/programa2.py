""" Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de 
    pedir el número hasta que no se introduzca correctamente."""

while True:
    num = int(input("Dame un numero entre 1 y 10 : "))
    if num > 10 or num < 1:
        print(f"El numero {num} no esta en el rango dicho, introduzcalo de nuevo.")
    else:
        print(f"El numero {num} esta en el rango ENHORABUENA")
        break