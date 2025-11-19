#Calcular el perímetro y área de un rectángulo dada su base y su altura
base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))
area= base * altura
perimetro= 2 * (base + altura)
print("El area es: " , area)
print("El perimetro: ", perimetro)