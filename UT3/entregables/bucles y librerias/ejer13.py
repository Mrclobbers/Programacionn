# Recorre el directorio actual y muestra el archivo con fecha de modificación más reciente.

# Para ello, investiga la función stat() que puedes aplicar sobre los archivos.

# Si no hay archivos, muestra “Sin archivos”.

# Librerías: from pathlib import Path
from pathlib import Path

fecha_ultima = 0.
ruta_actual = Path.cwd()
archivo = ""

for elem in ruta_actual.iterdir():
    if elem.is_file():
        fecha = elem.stat().st_mtime

        if fecha > fecha_ultima:
            fecha_ultima = fecha
            archivo_ultimo = elem.name

print(fecha_ultima, elem)