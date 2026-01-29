# Solicita por teclado 3 nombres de usuario mediante un bucle y almacénalos en una lista.
# A continuación, almacena sus home directory en un diccionario usando os.path.expanduser. 
# Muestra el contenido del diccionario recorriendo sus elementos
import os
lista = []
diccionario = {}

for a in range(3):
    nombres = input('Pon un nombre de usuario: ')
    lista.append(nombres)

for usuario in lista:
    diccionario[usuario] = os.path.expanduser(f'~{usuario}')

print("Directorios home de usuarios:")
for usuario, ruta in diccionario.items():
    print(f"{usuario}: {ruta}")
