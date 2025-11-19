#Dado un número entero de dos cifras, diseñe un algoritmo que permita obtener el número invertido utilizando operaciones aritméticas
# Ejemplo, si se introduce 23 que muestre 32
cifra= int(input("Pon un número de 2 cifras: "))
num1= cifra // 10
num2= cifra % 10
num3= (num2 * 10 + num1)
print("El número invertido sera: " , num3)