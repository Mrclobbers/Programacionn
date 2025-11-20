car = ""

while len(car) != 1: # Asegurarse de que el carácter es solo uno
    car = input("Introduce un carácter: ")

while car != " ":
    if car.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")
    break