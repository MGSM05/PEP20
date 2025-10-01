# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de N segundos. 
# Escribe un programa que determine la hora de llegada a la ciudad B.

hh = int(input("Introduce la hora de salida (HH): "))
mm = int(input("Introduce los minutos de salida (MM): "))
ss = int(input("Introduce los segundos de salida (SS): "))
viaje = int(input("Introduce el tiempo de viaje en segundos: "))

tiempoEnSegundos = (hh * 3600) + (mm * 60) + ss + viaje

hhLlegada = (tiempoEnSegundos // 3600) % 24
mmLlegada = (tiempoEnSegundos % 3600) // 60
ssLlegada = tiempoEnSegundos % 60

print("La hora de llegada es:", hhLlegada, ":", mmLlegada, ":", ssLlegada)