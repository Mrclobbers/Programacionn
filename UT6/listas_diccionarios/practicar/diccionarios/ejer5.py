#Crea un diccionario vacío.
#Luego, pide al usuario que introduzca por teclado 3 pares clave-valor para rellenarlo.
#Finalmente, imprime el diccionario.
diccionario = {}

for a in range(3):
    clave = input('Pon una clave: ')
    valor = int(input('Pon su valor: '))
    diccionario[clave] = valor
print(diccionario)