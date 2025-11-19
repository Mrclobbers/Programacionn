from pathlib import Path
import os

actual = Path.cwd()
C = os.listdir(actual)
print(C)
nueva = actual/"logs"

if nueva.exists():
    print("Ya existe")

else:
    nueva.mkdir()
    print("Carpeta creada")