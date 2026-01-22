# Elabora un pequeño programa que gestionará una lista de la compra.
# El programa mostrará un menú con las opciones disponibles. Las opciones son las siguientes:

# #Mostrar menu 
# print("\nGestión de Lista de la Compra") 
# print("1. Mostrar la lista") 
# print("2. Añadir elementos a la lista") 
# print("3. Borrar elementos de la lista") 
# print("4. Contar elementos de la lista") 
# print("5. Añadir una lista de elementos a la ya existente") 
# print("6. Borrar toda la lista") 
# print("7. Salir") 

# Se trata de implementar cada una de las acciones.
# La opción 2 añade un solo elemento a la lista,
# por ejemplo, leche, mientras que la opción 5 es capaz de añadir varios elementos a la lista de una vez,
# escritos separados por coma, por ejemplo, cereales,jamón,agua
print("\nGestión de Lista de la Compra") 
print("1. Mostrar la lista") 
print("2. Añadir elementos a la lista") 
print("3. Borrar elementos de la lista") 
print("4. Contar elementos de la lista") 
print("5. Añadir una lista de elementos a la ya existente") 
print("6. Borrar toda la lista") 
print("7. Salir") 

lista = [] # type: ignore

while True:
    opciones = int(input('Elige una opción: '))
    if opciones == 1:
        if len(lista) > 0:
            print(f'Tu lista de la compra {','.join(lista)}')
        else:
            print('La lsita esta vacia')
    elif opciones == 2:
        elemento = input('Pon un elemento: ')
        if elemento not in lista:
            lista.insert(1, elemento)
        else:
            print('Este elemento ya existe')
    elif opciones == 3:
        borrador = input('¿Que quieres borrar?: ')
        if borrador in lista:
            lista.remove(borrador)
        else:
            print('Este elemento no existe')

    elif opciones == 4:
        contador = len(lista)
        print(f'Tienes {contador} elementos en tu lista')
    
    elif opciones == 5:
        mas_elementos = input('Pon mas elementos: ')
        nueva_lista = mas_elementos.split(',')
        lista.extend(nueva_lista)

    elif opciones == 6:
        lista.clear()
    
    elif opciones == 7:
        break

    else:
        print('Esa opcion no esta, pon una opcion correcta')