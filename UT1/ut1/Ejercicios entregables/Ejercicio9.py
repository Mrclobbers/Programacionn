#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra
compra = float(input("La compra sin descuento es de: "))
descuento = 0.15
total = compra * (1 - descuento)
print("El cliente deberá pagar: ", total, "€ por su compra")
