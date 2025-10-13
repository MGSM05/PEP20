""" Mejora el programa anterior de forma que compruebe si el usuario está introduciendo 
    valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así 
    que pida muestre un aviso y vuelva a pedir el valor. """

import math


def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura


def mostrar_menu():
    print("\n1. Calcular el area de un CIRCULO")
    print("2. Calcular el area de un TRIANGULO")
    print("3. Calcular el area de un RECTANGULO")
    print("4. Salir")


def opcion1():
    while True:
        radio = float(input("Introduce el radio del CIRCULO: "))

        while radio < 0:
            radio = float(input("ERROR!! RADIO introducido invalido, introduzcalo de nuevo : "))

        area = calcular_area_circulo(radio)
        print(f"El area del CIRCULO es: {area}")
        break

def opcion2():
    while True:
        base = float(input("Introduce la base del TRIANGULO: "))

        while base < 0:
            base = float(input("ERROR!! BASE introducida invalida, introduzcala de nuevo: "))

        altura = float(input("Introduce la altura del TRIANGULO: "))
        
        while altura < 0:
            altura = float(input("ERROR!! ALTURA introducida invalida, introduzcala de nuevo: "))

        area = calcular_area_triangulo(base, altura)
        print(f"El área del TRIANGULO es: {area}")
        break

def opcion3():
    while True:
        base = float(input("Introduce la base del RECTANGULO : "))

        while base < 0:
            base = float(input("ERROR!! BASE introducida invalida, introduzcala de nuevo: "))

        altura = float(input("Introduce la altura del RECTANGULO : "))

        while altura < 0:
            altura = float(input("ERROR!! ALTURA introducida invalida, introduzcala de nuevo: "))

        area = calcular_area_rectangulo(base, altura)
        print(f"El área del RECTANGULO es: {area}")
        break


def main():
    opcion = 0
    while opcion != 4:
        mostrar_menu()
        opcion = int(input("Introduce una opcion (1-4) : "))

        match opcion:
            case 1:
                opcion1()
            case 2:
                opcion2()
            case 3:
                opcion3()
            case 4:
                print("Saliendo...")
            case _:
                print("Opcion no valida. Debe ser del 1 al 4.")

main()