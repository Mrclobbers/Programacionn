#Escribe un programa que cada vez que se ejecute pida por teclado una cantidad de
#segundos entre 0 y 10000 y que escriba su valor en horas, minutos y segundos
segundos = int(input("Pon una cantidad de segundos: "))

horas = (segundos // 3600)
minutos = (segundos // 60)
segundos2 = (segundos % 60)

print(f"EL tiempo sera de: {horas}", 'horas', minutos , 'minutos y', segundos2 , 'segundos')