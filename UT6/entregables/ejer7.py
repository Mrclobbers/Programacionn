# Usa la librería pathlib para listar los usuarios en /home. 
# Crea un diccionario con los nombres de cada usuario 
# y cuántos archivos tienen en su carpeta de usuario.
# Muestra el contenido del diccionario recorriendo sus elementos.
from pathlib import Path

usuarios = Path('/Users')
diccionario = {}

for usuario in usuarios.iterdir():
    if usuario.is_dir():
        archivos = list(usuario.iterdir())
        diccionario[usuario] = len(archivos)

for usuario, cantidad in diccionario.items:
    print(f'{usuario} : {cantidad} de archivos')