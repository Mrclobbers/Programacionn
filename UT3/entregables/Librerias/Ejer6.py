from pathlib import Path
import shutil

ejemplo = Path.cwd() / "config.example.ini"
destino = Path.cwd() / "config.ini"

if not destino.exists():
    if ejemplo. exists():
        shutil.copy(ejemplo, destino)
        print("Copiado")
    else:
        print("Falta fichero de ejemplo")
else:
    print("Ya existe")