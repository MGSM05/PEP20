# Escribe un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

f = float(input("Introduce la temperatura en grados FAHRENHEIT: "))

c = (f - 32) * 5 / 9

print(f ,"°F equivalen a " , round(c, 2) , "°C")