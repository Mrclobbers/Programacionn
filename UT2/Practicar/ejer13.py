#Solicita al usuario que ingrese una frase. Luego:
#Extrae e imprime los primeros 10 caracteres de la frase.
#Extrae e imprime los últimos 10 caracteres.
#Muestra todos los caracteres desde la posición 5 hasta la posición 15.
#Imprime la frase en orden inverso.
frase = input("Escribe una frase: ")
print(frase[:10])
print(frase[-10:])
print(frase[5:15])
print(frase[::-1])