#Realiza un programa que defina una lista llamada lista_numeros y la inicialice con 10 ceros.
#A continuación, recorre la lista y asigna a cada elemento un valor aleatorio (del 1 al 10).
#Posteriormente muestra en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
#Pista: recuerda que puedes generar números aleatorios con la función randint del módulo random
import random

lista_numeros = [0] * 10

for pos in range(len(lista_numeros)):
    lista_numeros[pos] = random.randint(1, 10)
    cuadrado = lista_numeros[pos] ** 2
    cubo = lista_numeros[pos] ** 3
    print(f"Número: {lista_numeros}, Cuadrado: {cuadrado}, Cubo: {cubo}")
