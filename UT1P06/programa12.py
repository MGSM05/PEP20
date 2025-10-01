# Sabiendo que 1 milla equivale a 1,61 Km, escribe un programa que pida un número de millas y un número de Km, 
# y muestre respectivamente el número de millas en km y el número de km en millas, redondeados a 2 decimales.

millas = float(input("Introduce el número de millas: "))
km = float(input("Introduce el número de kilómetros: "))

km_convertidos = millas * 1.61
millas_convertidas = km / 1.61

print(millas, "millas equivalen a", round(km_convertidos, 2), "km")
print(km, "km equivalen a", round(millas_convertidas, 2), "millas")