#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
#El programa debe determinar qué tipo de triangulo es, teniendo en cuenta los siguiente:

#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.
h1 = float(input("Pon el primer lado del tringulo: "))
c1 = float(input("Pon el segundo lado del tringulo: "))
c2 = float(input("Pon el tercer lado del tringulo: "))
if(h1 ** 2 == c1 ** 2 + c2 ** 2 or c1 ** 2 == h1 ** 2 + c2 ** 2 or c2 ** 2 == c1 ** 2 + h1 ** 2):
    print("Triangulo rectangulo")

if(h1 == c1 == c2):
    print("Triangulo equilátero")

elif(h1 == c1 or h1 == c2 or c1 == c2):
    print("Triangulo isósceles")

else:
    print("Triangulo escaleno")