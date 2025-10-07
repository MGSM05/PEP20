"""Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor 
o que indique que son iguales."""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El mayor es {num1} y el menor es {num2}.")
elif num2 > num1:
    print(f"El mayor es {num2} y el menor es {num1}.")
else:
    print("Los dos números son iguales.")