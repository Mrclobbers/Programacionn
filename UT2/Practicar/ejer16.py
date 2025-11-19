#Solicita al usuario que escriba una frase. Luego:
#Reemplaza todas las vocales (a, e, i, o, u) con asteriscos (*).
#Imprime la frase original y la frase modificada.
frase = input("Escribe una frase: ")
frase_new= frase.replace('a', '*')
frase_new= frase_new.replace('e', '*')
frase_new= frase_new.replace('i', '*')
frase_new= frase_new.replace('o', '*')
frase_new= frase_new.replace('u', '*')
print(frase_new)
print(frase)