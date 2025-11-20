import sys
import shutil

if len(sys.argv) >= 2:
    umbral = int(sys.argv[1])
else:
    umbral = 85
    
total, usado, libre = shutil.disk_usage("/")
espacio = round(usado * 100 / total)

if espacio >= umbral:
    print("OK")
else:
    print("ALERTA")
