"""Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no 
    es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o 
    negativo) y si el valor no es correcto, mostrará un aviso."""

par = int(input("Dame un numero PAR : "))

if (par % 2 == 0):
    impar = int(input("Dame un numero IMPAR : "))
else:
    print("Has introducido un numero que no es PAR")

if (impar % 2 == 0):
    print("Has introducido un numero que no es IMPAR")