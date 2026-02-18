# Vamos a realizar un análisis de las siguientes rutas críticas del sistema:
# rutas = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]
# Guarda en un diccionario si cada una existe y si es un archivo, un directorio o no existe.
# Muestra un informe con el sistema operativo, número de CPUs, fecha actual y el estado de cada ruta.
# Usa las librerías pathlib, platform, os y datetime
import platform
from pathlib import Path
from datetime import datetime,timedelta
import os

rutas = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]
estado_rutas = {}

for i in rutas:
    ruta = Path(i)
    if ruta.exists():
        if ruta.is_dir:
            estado_rutas[i] = 'Directorio'
        elif ruta.is_file:
            estado_rutas[i] = 'Carpeta'
        else:
            estado_rutas[i] = 'Otro'
    else:
        estado_rutas[i] = 'No existe'

print(f"Análisis del sistema ({platform.system()}, CPUs: {os.cpu_count()})")
print(f"Fecha del informe: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Estado rutas: ")
for ruta, estado in estado_rutas.items():
    print(f"{ruta}: {estado}")