# Una tienda ofrece un descuento del 15% sobre el total de la compra. Un cliente desea saber cuánto deberá pagar 
# finalmente por su compra.

total = float(input("Introduce el total de la compra: "))

descuento = total * 0.15
pago_final = total - descuento

print("El cliente deberá pagar:", round(pago_final, 2))