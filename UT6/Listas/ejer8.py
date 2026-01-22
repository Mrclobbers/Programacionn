#Queremos guardar los nombres y las edades de los alumnos de un curso.
#Para ello utilizarás dos listas, una para nombres y otra para edades.
#Realiza un programa que introduzca el nombre y la edad de cada alumno.
#El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*)
#Al finalizar se mostrará los siguientes datos:

#Todos los alumnos mayores de edad (su nombre y edad).
#Los alumnos mayores, es decir, los que tienen más edad (su nombre y edad).
nombres = []
edades = []

while True:
    n = input("Nombre: ")
    if n == '*':
        break
    nombres.append(n)
    e = int(input("Edades: "))
    edades.append(e)

for a in range(len(edades)):
    if edades[a] >= 18:
        print(f'Los mayores de edad son {nombres[a]} y su edad es {edades[a]}')

m = max(edades)
for a in range(len(edades)):
    if edades[a] == m:
        print(f'Los mayores de edad son {nombres[a]} y su edad es {edades[a]}') 