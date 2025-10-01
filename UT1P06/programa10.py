# Escribe un programa que dado un número de dos cifras, obtenga el número invertido.

numero = int(input("Introduce un numero de dos cifras: "))

decenas = numero // 10
unidades = numero % 10

numero_invertido = unidades * 10 + decenas

print("El número invertido es:", numero_invertido)