""" Escribe un programa que pida un número y muestre una lista de números desde 1 al 
    número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se 
    pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto."""

num = int(input("Introduce un numero del 1 al 10 : "))

while (num > 10 or num < 1):
    num = int(input("Numero INCORRECTO, introduzcalo otra vez : "))

    if num >= 1 and num <= 10:
        print("Numero BIEN introducido")

for i  in range(0, num):
    print(i + 1)