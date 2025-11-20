#Mantenimiento en fin de semana

#Pistas: librería datetime

#Realiza un programa que averigue qué día de la semana es el día actual y muestre
#“Ventana de mantenimiento” si es sábado (día 5) o domingo (día 6).
#En caso contrario, muestra “Operación normal”.
from datetime import datetime

dia = datetime.now().weekday()

if dia == 5 or dia == 6:
    print("Mantenimiento")
else:
    print("Normal")