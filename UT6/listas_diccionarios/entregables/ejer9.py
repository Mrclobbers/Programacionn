# Vas a simular la gestión de la variable de entorno PATH,
# que contiene varias rutas separadas por : (dos puntos).
# A partir de un string que representa un PATH,
# por ejemplo, "/usr/local/bin:/usr/bin:/bin" conviértelo en una lista,
# añade una nueva ruta al final (pídela por teclado), otra al inicio (pídela por teclado),
# y luego vuelve a unirlo en un solo string.
# Muestra cada una en una línea y luego muestra el resultado final.
from pathlib import Path


ruta_path = ["/usr/local/bin:/usr/bin:/bin"]
primero = input('Pon una ruta para el inicio: ')
ultimo = input('Pon una ruta para el final: ')

ruta_path.insert(0, primero)
ruta_path.append(ultimo)

ruta_path = ':'.join(ruta_path)
print(ruta_path)
ruta_path = ruta_path.split(':')
print(ruta_path)