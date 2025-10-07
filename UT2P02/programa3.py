dividendo = int(input("Dime el dividendo : "))
divisor = int(input("Dime el divisor : "))

if (divisor  == 0):
    print ("No se puede dividir por 0")
else:
    division = dividendo / divisor
    print ("La division entre " , dividendo , " y " , divisor , " da : " , round(division, 2))
