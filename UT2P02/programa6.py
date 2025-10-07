"""Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta"""

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

valida = True  

if mes < 1 or mes > 12:
    valida = False
else:
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            dias_mes = 31
        case 4 | 6 | 9 | 11:
            dias_mes = 30
        case 2:
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                dias_mes = 29
            else:
                dias_mes = 28
        case _:
            valida = False  

    if not (1 <= dia <= dias_mes):
        valida = False

if valida:
    print("La fecha es correcta.")
else:
    print("La fecha no es válida.")