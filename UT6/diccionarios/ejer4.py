# Escribe un programa que solicite al usuario una palabra y devuelva su significado usando el siguiente diccionario:
# diccionario = {
#     'python': 'Lenguaje de programación',
#     'algoritmo': 'Conjunto de instrucciones',
#     'variable': 'Espacio de memoria para almacenar datos'
# }
# Nota: Debes controlar correctamente si el usuario introduce una palabra que no existe.
diccionario = {
    'python': 'Lenguaje de programación',
    'algoritmo': 'Conjunto de instrucciones',
    'variable': 'Espacio de memoria para almacenar datos'
}
while True:
    palabra = input('Pon un nombre del diccionario: ')

    if palabra in diccionario:
        print(f'La palabra {palabra}, significa{diccionario[palabra]}')
        break
    else:
        palabra = input('Esa palabra no esta en el diccionario.Pon un nombre del diccionario: ')