#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos
#Escribir un algoritmo que determine la hora de llegada a la ciudad B
hpartida = int(input("Hora de salida (HH): "))
mpartida = int(input("Minutos de salida (MM): "))
spartida = int(input("Segundos de salida (SS): "))
sviaje = int(input("Tiempo que has tardado en segundos: "))

sinicial= hpartida * 3600 + mpartida * 60 + spartida
sfinal= sinicial + sviaje

hllegada = (sfinal // 3600) % 24
mllegada = (sfinal % 3600) // 60
sllegada = (sfinal % 3600) % 60

print(f"Llegara a las: {hllegada:02}:{mllegada:02}:{sllegada:02}")