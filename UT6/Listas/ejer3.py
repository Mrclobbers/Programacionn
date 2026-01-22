#Realiza un programa que lea por teclado las 5 notas obtenidas por un alumno.
#Debes controlar que las notas estén comprendidas entre 0 y 10 y pueden contener decimales. 
#A continuación, debe mostrar todas las notas indicando su orden, es decir,
#“Nota 1: 5.5, Nota 2: 6, …”, debe mostrar también la nota media, la nota más alta que ha sacado y la menor.
lista_cadenas = []

for i in range(0,5):

    cadena = float(input(f"Introduce la nota {i + 1}: "))

    while cadena < 0 and cadena > 10:
        print('Nota no valida, pon otra: ')

    else:
        lista_cadenas.append(cadena)
    print(f"Nota {i}: {lista_cadenas}")