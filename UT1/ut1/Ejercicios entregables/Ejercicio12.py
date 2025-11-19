#Pide al usuario dos pares de números x1, y1 y x2, y2, que representen dos puntos en el plano
#Calcula y muestra la distancia entre ellos
import math
x1= float(input("Pide el numero x1: "))
y1= float(input("Pide el numero y1: "))
x2= float(input("Pide el numero x2: "))
y2= float(input("Pide el numero y2: "))
distancia= math.sqrt((x2 - x1)** 2 + (y2 - y1)** 2)
print(f"distancia: {distancia:.2f}")