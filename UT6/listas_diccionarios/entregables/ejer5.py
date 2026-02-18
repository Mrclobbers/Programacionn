# Crea 3 nombres de carpeta que se situarán en el directorio actual en una lista y convierte a tipo Path. 
# A continuación,
# para cada carpeta, si no existe, la creas y guarda en un diccionario si las carpetas fueron creadas o ya existían. 
# Muestra el contenido del diccionario recorriendo sus elementos.
from pathlib import Path

diccionario = {}
lista = ['carpeta1', 'carpeta2', 'carpeta3']

for nombre in lista:
    ruta = Path(nombre)
    
    if not ruta.exists():
        ruta.mkdir()
        diccionario[ruta] = 'Creada'
    else:
        diccionario[ruta] = 'Existe'

for carpeta, estado in diccionario.items():
    print(f'{carpeta} : {estado}')
