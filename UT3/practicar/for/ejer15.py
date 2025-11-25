#Una empresa les paga a sus empleados en base a las horas trabajadas durante la semana.
#Realizar un programa para determinar el sueldo semanal de cada uno de los N trabajadores
#y, además, calcular cuánto pagó la empresa por los N empleados en total

#Pista: habrá que preguntar cuántos trabajadores tiene la empresa y cuánto es el sueldo por hora.
#Además, para cada trabajador, tendrás que preguntar cuántas horas trabaja a la semana para calcular su sueldo.
horas_total = 0

trabajadores = int(input("Cuantos trabajadores tiene tu empresa?: "))
precio_hora = int(input("Cuanto cobras la hora?: "))

for dia in range(1, trabajadores):
    horas = int(input(f"Cuantas horas trabajaste trabajador numero {dia} ?: "))
    horas_total += horas
    sueldo_sem = horas * precio_hora
    print(f"El trabajador {dia} cobra {sueldo_sem}")
print(f"La empresa paga: {horas_total * sueldo_sem}")
