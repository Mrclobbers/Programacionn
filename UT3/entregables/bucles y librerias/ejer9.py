# Vamos a crear una carpeta para un aula determinada, y dentro de esa carpeta, crearemos una carpeta para cada PC.

# Pide el nombre del aula (texto cualquiera) y un número de equipos M.

# Crea las carpetas: <AULA>/PC-01, <AULA>/PC-02 … <AULA>/PC-0M utilizando la librería pathlib.

# Usa un bucle for para generar los números de los PCs formateados con dos dígitos mediante la función zfill.

# Tanto si ya existe la carpeta como si no, debes indicarlo. En caso de que la carpeta no exista la creas.

# Librerías: from pathlib import Path
from pathlib import Path

aula = input("Pon una aula: ")
equipos = int(input("Pon el numero de equipos en ese aula: "))
ruta_actual = Path.cwd()

carpeta_aula = ruta_actual / aula

if carpeta_aula.exists():
    print("Esta carpeta ya existe")
else:
    carpeta_aula.mkdir()

for i in range(1, equipos + 1):
    carpeta_pc = carpeta_aula / ("PC-" + str(i).zfill(2))
    carpeta_pc.mkdir()

print("Carpetas creadas")


