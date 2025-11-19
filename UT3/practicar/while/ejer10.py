import random
numl = random.randrange(1, 100)

num_respuesta = int(input("Pon tu respuesta: "))
cont_intentos = 1

while numl != num_respuesta and cont_intentos == 11:
    if num_respuesta < numl:
        print("El numero es mayor")
        cont_intentos += 1
    else:
        print("El numero es menor")
        cont_intentos += 1
    num_respuesta = int(input("Incorrecto, pon otro numero: "))
else:
    print(f"El numero es correcto y era: {numl} y lo lograte en: {cont_intentos} intentos")
