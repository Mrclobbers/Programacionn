#Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Utiliza potencias para ello. 
num1= float(input("Tunumero es: "))
raiz2= (num1 **0.5)
raiz2_2= round(raiz2, 2)

raiz3= (num1 **(1/3))
raiz3_2= round(raiz3,2)

print("La raiz cuadra es: " , raiz2_2)
print("La raiz cubicaes", raiz3_2)