""" Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el 
    ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia 
    continue."""

print("\nCON BUCLE FOR : ")
for i in range(0, 11):
    if i % 2 == 0:
        print(i)

print("\nCON BUCLE FOR Y CONTINUE: ")
for i in range(0, 11):
    if i % 2 != 0:
        continue
    print(i)

print("\nCON BUCLE WHILE : ")
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

print("\nCON BUCLE WHILE Y CONTINUE: ")
i = 0
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1