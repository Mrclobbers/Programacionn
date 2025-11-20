import random
numl = random.randrange(1, 100)

num_respuesta = int(input("Pon tu respuesta: "))
cont_intentos = 1

while numl != num_respuesta and cont_intentos < 11:
    if cont_intentos == 10:
        print(f"Te quedaste sin intentos, el numero era {numl}")
        break
    if num_respuesta < numl:
        print("El numero es mayor")
        cont_intentos += 1
        num_respuesta = int(input("Incorrecto, pon otro numero: "))
    else:
        print("El numero es menor")
        cont_intentos += 1
        num_respuesta = int(input("Incorrecto, pon otro numero: "))

    if numl == num_respuesta:
        print(f"El numero es correcto y era: {numl} y lo lograte en: {cont_intentos} intentos")
else:
    if num_respuesta == numl:
        print(f"El numero es correcto y era: {numl} y lo lograte en: {cont_intentos} intentos")
   
