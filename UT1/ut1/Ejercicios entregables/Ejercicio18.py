#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales
nombre= input("Pon tu nombre: ")
apellido1= input("Pon tu primer apellido: ")
apellido2= input("Pon tu segundo apellido: ")
iniciales = (nombre[0] + apellido1[0] + apellido2[0]).upper()
print(f"Tus iniciales son: {iniciales}")