resultado = 1
contador = 2

num = int(input("Dime un número: "))

if num != 0:
    for num in range(1,num):
        resultado *= contador
        contador += 1
    print (f"El factorial es {resultado}")

else:
    print("El factorial es 0")