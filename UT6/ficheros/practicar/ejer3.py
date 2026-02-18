with open("numeros.txt", "w") as archivo:
    for a in range(1, 11):
        archivo.write(str(a) + "\n")
