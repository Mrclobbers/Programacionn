#Escribe un programa que cuente cuántas veces aparece cada letra en una palabra introducida por el usuario.
#Usa un diccionario para almacenar el resultado.
#Ejemplo: en la palabra ‘amiga’ la ‘a’ aparece 2 veces, la ‘m’ 1 vez, la ‘i’ 1 vez y la ‘g’ 1 vez.
palabra = input("Introduce una palabra: ")

contador_letras = {}

for letra in palabra:
    if letra in contador_letras:
        contador_letras[letra] += 1
    else:
        contador_letras[letra] = 1

print("Conteo de letras:")
for letra, cantidad in contador_letras.items():
    print(f"La letra '{letra}' aparece {cantidad} veces")
