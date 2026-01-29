# Pide al usuario 4 nombres de archivo o directorio.
# Usa la librería pathlib para determinar si existen y su tipo (fichero o directorio)
# y almacena esa información en un diccionario.
# Es decir, el diccionario debe contener para cada ruta si es archivo, directorio o si no existe.
# Muestra el contenido del diccionario recorriendo sus elementos.
from pathlib import Path
diccionario = {}
ruta = Path.cwd()

for a in range(4):
    nombre = Path(input ('Pon un nombre de directorio/archivo: '))
    if nombre.exists():
        if nombre.is_dir():
            diccionario[a] = 'Directorio'
        elif nombre.is_file():
            diccionario[a] = 'Archivo'
        else:
            diccionario[a] = 'Otro tipo'
    else:
        diccionario[a] = 'No existe'

for nombre, valor in diccionario.items():
    print(f'{nombre} : {valor}')
