# Pide un número N por teclado y crea carpetas backup_1 … backup_N en el directorio actual.

# Si alguna ya existe, no pasa nada. Indica para cada carpeta si la creas o si ya existía.

# Librerías: from pathlib import Path
from pathlib import Path

num = int(input("Pon un numero: "))
ruta_actual = Path.cwd()

for i in range(1, num + 1):
    ruta_backup = ruta_actual / f"backup_{i}"  # Carpetas numeradas

    if ruta_backup.exists():
        print(f"La carpeta {ruta_backup} ya existe")
    else:
        ruta_backup.mkdir()
        print(f"Carpeta {ruta_backup} creada")

print("Proceso terminado")
