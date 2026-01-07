#Ejer1: Dice el numero mas grande entre 2
from modulo_guille import *

print("prueba ejer1")
x=4
y=6
print(f"Parametros de entrada: {x}, {y}")

may = mayor(x, y)

print(f"El mayor entre {x} y {y} es: {may}")

#Ejer3: Te dice si el numero es par o impar

print("prueba ejer3")
a=3
print(f"Parametros de entrada: {a}")

es = es_par(a)

if es:
    print(f"El numero {a} es par")
else:
    print(f"El numero {a} es impar")

#Ejer6: Saber si es mayuscula o no

print("prueba ejer6")
letra ='l'
print(f"Parametros de entrada: {letra}")

mayus = es_mayusculas(letra)

if mayus:
    print(f"La letra {letra} esta en mayuscula")
else:
    print(f"La letra {letra} esta en minuscula")

#Ejer7: calcular la potencia

print("prueba ejer7")
base = 2
exp = 4
print(f"Parametros de entrada: base = {base} y  exponente = {exp}")

pot = potencia(base, exp)

if pot:
    print(f'Tu potencia es igual a: {pot}')

#Ejer9: ordenar numeros
print("prueba ejer9")
n1 = 3
n2 = 2
n3 = 1
print(f"Parametros de entrada: numero 1 = {n1}, numero 2 = {n2} y numero 3 = {n3}")

orden = es_mayor(n1, n2, n3)

if orden:
    print(f"El orden es: {orden}")

#Ejer10: Función clasifica_circunferencias(x1, y1, r1, x2, y2, r2)
#que recibe como argumentos los centros (x,y) y radios r de dos circunferencias
#y las clasifica en uno de estos estados: exteriores, tangentes exteriores, secantes, tangentes interiores, interiores o concéntricas. Nota: 
#esta función no devuelve nada, simplemente imprime el tipo de circunferencias
print("prueba ejer10")
x1 = 3
x2 = 2
y1 = 23
y2 = 10
r1 = 55
r2 = 37 
print(f"Parametros de entrada: X1 = {x1}, X2 = {x2}, Y1 = {y1}, Y2 = {y2}, R1 = {r1} y R2 = {r2}")

clac = clasifica_circunferencia(x1, x2, y1, y2, r1, r2)
if clac:
    print(f"Tu circunferencia es: {clac}")