# Escribe un programa que calcule la calificación de estudiante en un módulo. 
# La calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2 60%, RA3 20%).

ra1 = float(input("Introduce la calificacion de RA1: "))
ra2 = float(input("Introduce la calificacion de RA2: "))
ra3 = float(input("Introduce la calificacion de RA3: "))

calificacion_final = ra1 * 0.2 + ra2 * 0.6 + ra3 * 0.2

print("La calificacion final del estudiante es:", round(calificacion_final, 2))