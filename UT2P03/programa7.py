""" Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la 
    suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza 
    la instrucción break y otra no."""

sumador = 0
contador = 0

num = int(input("Introduce cualquier numero, pulsa 0 para salir : "))

while (num != 0):
    sumador = sumador + num
    contador = contador + 1
    num = int(input("Introduce cualquier numero, pulsa 0 para salir : "))

print(f"\nLa suma de todos los numero introducidos es de {sumador}")
print(f"La media de los números introducidos es {sumador / contador}")