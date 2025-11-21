suma = 0
cont = 0

for num in range(1000):
    num = int(input("Número (0 para salir): "))
    if num == 0:
        print("Sales del bucle")
        break
    suma += num
    cont += 1
print(f"La suma es igual a : {suma}")
print(f"La media es igual a: {suma/cont}")
    