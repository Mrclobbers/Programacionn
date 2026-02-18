#Queremos guardar la temperatura mínima y máxima de los 7 días de la semana pasada en dos listas.
#Para ello pide las temperaturas por teclado. Realiza un programa que dé la siguiente información:

#Calcule la temperatura media de cada día.

#Calcule los días con menos temperatura.

#lea una temperatura por teclado y se muestre los días cuya temperatura máxima coincide con ella. 
#Si no existe ningún día se mostrará un mensaje informativo.

# Nota: Como implementación básica, nos podemos referir a los días por su número
#(por ejemplo, el día 1 el lunes, el 2 es martes, etc).
#Si queréis mejorar el programa, nos referiremos por su nombre (lunes, martes, etc.)
maxima = []
minima = []
media = []

for i in range(0,7):
    n = float(input('Pon la temperatura minima de cada dia: '))
    minima.append(n)
    e = float(input('Pon la temperatura maxima de cada dia: '))
    maxima.append(e)
    media.append(n + e/2)
    print(f'La media de cada dia es {media[i]}')

menos_temperatura = min(minima)
for i in range(len(minima)):
    if minima[i] == menos_temperatura:
        print(f'Los dias con menos temperatura son: {minima[i]}')

temp_max = float(input('Pide una temperarura adicional: '))
if temp_max == maxima[i]:
    print(f'La temperatura {temp_max} coincide con {maxima[i]}')



