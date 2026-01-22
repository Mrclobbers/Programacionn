#Dado el diccionario anterior, muestra por pantalla si el producto 'pan' está en el diccionario.
#Haz lo mismo con 'queso'.
productos = {'manzana': 1.5, 'pan': 0.8, 'leche': 1.2}

pan = productos.get('pan')
queso = productos.get('queso', 'No disponible')

print(pan)
print(queso)
