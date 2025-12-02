# Genera mediante un bucle 7 nombres de ficheros backup a partir de hoy en formato backup_AAAA_MM_DD.zip e imprímelos.

# Es decir, backup_2025_11_15.zip, backup_2025_11_16.zip, etc.

# Librerías: from datetime import datetime, timedelta

from datetime import datetime, timedelta
d = datetime.now()

for Backup in range(0,7):
    mañana = d + timedelta(days = Backup)
    print(mañana.strftime('Backup_%Y_%m_%d.zip'))