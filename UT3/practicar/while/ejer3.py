inte = 1
cant = int(input("Dame una cantidad de numeros: "))
cont_mayor = 0
cont_menor = 0
cont_iguales = 0

while inte <= cant:
    num = int(input("Dame un numero: "))
    if num == 0:
        cont_iguales += 1
        inte += 1
    elif num > 0:
        cont_mayor += 1
        inte += 1
    else:
        cont_menor += 1
        inte += 1


print(f'Numeros mayores a 0: {cont_mayor}, numeros menores a 0: {cont_menor}, numeros iguales a 0: {cont_iguales}')
