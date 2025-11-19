#Escribe un programa que pida una frase por teclado. Realiza las siguientes tareas:
#1. Imprime el número de caracteres del texto.
#2. Imprime si el texto contiene la vocal ‘a’ (devolviendo True o False)
#3. Imprime el texto sin espacios al principio y al final.
#4. Muestra los últimos 5 caracteres (utiliza el troceado de cadenas).
frase = input("Escribe una frase: ")

caracteres = len(frase)

vocal= 'a' in frase

espacios = frase.strip()

final = espacios[-5 :]

print(caracteres)
print(vocal)
print(espacios)
print(final)