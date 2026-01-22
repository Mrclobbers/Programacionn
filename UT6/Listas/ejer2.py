#Crea una lista de 5 elementos donde cada elemento sea una cadena que se pide por el teclado.
#Copia los elementos de la lista en otra lista, pero en orden inverso, y muestra los elementos invertidos por la pantalla.

lista_cadenas = []

for i in range(5):
    cadena = input(f"Introduce la cadena {i + 1}: ")
    lista_cadenas.append(cadena)
    lista_inversa = list(reversed(lista_cadenas))

print(lista_cadenas)
print(lista_inversa)



