# Muestra un menú en bucle con opciones:

# 1) Listar archivos del directorio actual 2) Crear carpeta ‘logs’ 3) Salir

# Usa while True y condicionales para implementar cada una de las opciones.

# Librerías: from pathlib import Path
from pathlib import Path

while True:
    cuestion = int(input("Que opcion elijes?: "))
    if cuestion == 1:
        for directorio in Path.cwd().iterdir():
            print(directorio)
    elif cuestion == 2:
        if Path("logs").is_dir():
            print("Ya existe la carpeta logs")
        else:
            Path.mkdir("logs")
    elif cuestion == 3:
        break
    else:
        print("No pusiste ninguna de las 3 opciones")

 