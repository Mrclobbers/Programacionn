# Genera un informe system_report.txt con la fecha/hora actual, 
# el sistema operativo detectado (platform) y el número de CPUs (os.cpu_count()).
import os
import platform
from datetime import datetime

with open("system_report.txt", "a") as archivo:
    archivo.write(platform.system() + "\n")
    archivo.write(str(os.cpu_count()) + "\n")
    archivo.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
