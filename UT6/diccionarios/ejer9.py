#Escribe un programa que lea 5 frases introducidas por el usuario y almacene en un diccionario cuántas veces aparece cada palabra.
#Ignora mayúsculas/minúsculas.
diccionario = {} # type: ignore
vacio =''

for _ in range(5):
    frases = input('Escribe palabras: ')
    frases = frases.lower()
    frases_f = frases.split()


    for i in frases_f:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
print(diccionario)