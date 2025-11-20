#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d
#El que está detrás viaja a una velocidad mayor
#Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h)
#Y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro
v1= float(input("La velocidad del primer coche es de (km):"))
v2= float(input("La velocidad del segundo coche es de (km):"))
distancia= float(input("la distancia es de (km/h): "))

num1= distancia / (v2-v1) *60
num1_2= round(num1, 2)
print("El tiempo que tardara es de:", num1_2, "minutos")