# Simula una configuración en service.conf guardando en el fichero líneas clave=valor.
# Por ejemplo: port=8080, mode=prod, user=admin. Léelo y crea un diccionario.
# Luego pregunta una clave por teclado y muestra su valor o un mensaje si no existe.
diccionario = {

}

with open("service.conf", "w") as f:
    f.write("port=8080\nmode=prod\nuser=admin\n")

with open("service.conf", "r") as f:
    for linea in f:
        
        clave, valor = linea.strip().split("=")
        diccionario[clave] = valor

buscador = input("Pon una clave: ")

if buscador in diccionario:
    print(f"El valor es {diccionario[buscador]}")

else:
    print("No existe")