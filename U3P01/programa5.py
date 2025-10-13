""" Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables 
    en Python (globales, no locales y locales)."""

x = 10

def funcion_global():
    global x
    print("Valor INICIAL : ", x)
    x = 20
    print("Vlor CAMBIADO : ", x)

def funcion_local():
    y = 5
    print("Valor de y en variable LOCAL : ", y)
    print("Valor de x en variable GLOBAL :", x)

def funcion_no_local():
    z = "HOLA"

    def interna():
        nonlocal z 
        print("z significa : ", z)
        z = "ADIOS"
        print("Se ha modificado z a :", z)

    interna()

print("VALOR ORIGINAL DE X : ", x)
funcion_local()
funcion_global()
print("VALOR DE X CAMBIADA, AL LLAMAR A UNA FUNCION : ", x)
funcion_no_local()
