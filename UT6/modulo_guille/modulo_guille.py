import math
#Ejercicio 1
def mayor(num1, num2):

    if num1 > num2:
        return num1

    else:
        return num2
    
x = mayor(4, 5)

y = mayor(10, 1)

#Ejercicio 3
def es_par(n):

    if n % 2 == 0:
        return True
    else:
        return False

#Ejercicio 6
def es_mayusculas(cad):

    if cad.isupper():
        return True

    else:
        return False

#Ejercicio 7
def potencia(base, exponente):

    if exponente > 0:
        return base ** exponente

    elif exponente < 0:
        return 1/ (base ** abs(exponente))

    elif exponente == 0:
        return 1
    
#Ejercicio 10
def es_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            return (num1, num2, num3)
        else:
            return (num1, num3, num2)
    elif num2 >= num1 and num2 >= num3:
        if num1 >= num3:
            return (num2, num1, num3)
        else:
            return (num2, num3, num1)
    else:
        if num1 >= num2:
            return (num3, num1, num2)
        else:
            return (num3, num2, num1)
 #Ejercicio 10
def clasifica_circunferencia(x1, x2, y1, y2, r1, r2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if distancia > (r1 + r2):
        return ("Circunferencias exteriores")
    elif distancia == (r1 + r2):
        return ("Circunferencias tangentes exteriores")
    elif distancia < (r1 + r2) and distancia > abs(r1 - r2):
        return ("Circunferencias secantes")
    elif distancia == abs(r1 - r2):
        return ("Circunferencias tangentes interiores")
    elif distancia > 0 and distancia < abs(r1 - r2):
        return ("Circunferencias interiores")
    elif distancia == 0:
        return ("Circunferencias concéntricas")

