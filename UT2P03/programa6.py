""" Escribe un programa  que realice las siguientes operaciones:
        • Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que 
        no se introduzca el número correcto.
        • Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
        • Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si 
    desea introducir otro número o no. Si el usuario selecciona que quiere continuar el 
    programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario 
    indica que no quiere continuar el programa finaliza"""

continuar = "s"

while continuar.lower() == "s":
    num = int(input("Introduce un numero del 1 al 10 : "))

    while (num > 10 or num < 1):
        num = int(input("Numero INCORRECTO, introduzcalo otra vez : "))

        if num >= 1 and num <= 10:
            print("Numero BIEN introducido")

    for i  in range(0, 11):
        print(f"{i} X {num} = {i * num}")

    continuar = input("\n¿Deseas introducir otro número? (s/n): ")