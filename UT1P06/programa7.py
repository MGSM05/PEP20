# Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a cuántas horas y minutos corresponde.

total = int(input("Introduce la cantidad de minutos: "))

horas = total // 60
minutos = total % 60

print(total, "minutos corresponden a", horas, "horas y", minutos, "minutos")