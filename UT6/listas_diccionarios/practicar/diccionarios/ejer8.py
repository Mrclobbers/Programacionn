#Dado un diccionario con nombres de personas como claves y su edad como valores, muestra el nombre de la persona más joven.
#Crea tú mismo el diccionario con al menos 3 pares clave-valor.
personas = {
    'Guille' : 18, 
    'Daniel' : 19, 
    'Mauro' : 33
    }

vacio = ''

for i in personas:
    if vacio == '':
        vacio == i
    elif personas[vacio] > personas[i]:
        vacio == i
print(i)