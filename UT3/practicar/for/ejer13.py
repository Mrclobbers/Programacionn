#Una empresa quiere tener el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) 
#para determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.
#Por tanto, deberás pedir por teclado cuantas horas ha trabajado cada día, así como a cuánto cobra la hora.
#El precio por hora es único.
horas_total = 0.0

precio_hora = float(input("Cuanto cobras la hora?: "))

for dia in range(1,7):
    horas = float(input(f"Cuantas horas trabajaste el dia {dia} ?: "))
    horas_total += horas
sueldo_sem = horas_total * precio_hora

print(horas_total)
print(sueldo_sem)


