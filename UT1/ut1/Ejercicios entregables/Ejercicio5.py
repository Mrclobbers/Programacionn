#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: 
# C = (F-32)*5/9
gradosF= float(input("Grados en Fahrenheit: "))
celsius= (gradosF - 32) * 5/9
celsius2= round(celsius, 2)
print("En grados en Celsius: ", celsius2)