from datetime import datetime

hora = datetime.now().hour

if hora < 12:
    print("Backup de mañana")

elif 12 <= hora < 20:
    print("Backup de tarde")

elif hora >= 20:
    print("Backup nocturno")


