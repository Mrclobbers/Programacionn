#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa
cateto1 = float(input("Ingresa el primer cateto: "))
cateto2 = float(input("Ingresa el segundo cateto: "))
hipotenusa= (cateto1 ** 2 + cateto2 **2) ** 0.5
hipotenusa2= round(hipotenusa, 2)
print(hipotenusa2)