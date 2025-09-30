# Escribe un programa que use varias veces la función printf() para 
#  Mostrar las operaciones del los operadores aritméticos de Python entre dos 
#  números.
#  Mostrar las operaciones de los operadores lógicos de Python con valores 
#  booleanos.
#  Mostrar las operaciones de los operadores de comparación de Python con valores 
#  booleanos y/o números

a = 30
b = 40

print(a , "+" , b , " = " , (a + b))
print(a , "-" , b , " = " , (a - b))
print(a , "*" , b , " = " , (a * b))
print(a , "/" , b , " = " , (a / b))
print(a , "//" , b , " = " , (a // b))
print(a , "%" , b , " = " , (a % b))
print(a , "**" , b , " = " , (a ** b) , "\n")

x = True
y = False

print(x , " AND " , y , " = " , (x and y))
print(x , " OR " , y , " = " , (x or y))
print("NOT " , x , " = " , (not x))
print("NOT " , y , " = " , (not y) , "\n")

print(a , " == " , b , " = " , (a == b))
print(a , " != " , b , " = " , (a != b))
print(a , " > " , b , " = " , (a > b))
print(a , " < " , b , " = " , (a < b))
print(a , " >= " , b , " = " , (a >= b))
print(a , " <= " , b , " = " , (a <= b))
print(x , " == " , y , " = " , (x == y))
print(x , " != " , y , " = " , (x != y))
