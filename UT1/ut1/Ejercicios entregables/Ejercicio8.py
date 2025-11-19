#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas
#El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes 
#Tomando en cuenta su sueldo base y comisione
sueldobase = float(input("Su sueldo base es de: "))
venta1 = float(input("La primera venta es de: "))
venta2 = float(input("La segunta venta es de: "))
venta3 = float(input("La tercera venta es de: "))
porcentaje = 0.10

total_ventas = venta1 + venta2 + venta3
comision = total_ventas * porcentaje
total = sueldobase + comision
print("Comisión obtenida: ", comision, "€")
print("Total recibido en el mes: ", total, "€")
