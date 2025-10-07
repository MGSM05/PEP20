""" Escribe un programa que pida primero un número par y luego un número impar (positivos 
    o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o 
    impar respectivamente), se mostrará un aviso."""

par = int(input("Dame un numero PAR : "))
impar = int(input("Dame un numero IMPAR : "))

if (par % 2 != 0):
    print ("Has introducido un numero que no es PAR")

if (impar % 2 == 0):
    print("Has introducido un numero que no es IMPAR")