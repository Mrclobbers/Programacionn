# Usa pathlib para listar los archivos y carpetas del directorio actual y guarda esa información 
# (si son archivo o directorio) en un diccionario, tal y como se ha hecho en el ejercicio anterior.
from pathlib import Path

ruta = Path('.')
elementos = list(ruta.iterdir())
diccionario = {}

for i in elementos:
    if i.is_file():
        diccionario[i] = 'Archivo'
    elif i.is_dir():
        diccionario[i] = 'Directorio'

for elementos, valores in diccionario.items():
    print(f'{elementos} : {valores}')
