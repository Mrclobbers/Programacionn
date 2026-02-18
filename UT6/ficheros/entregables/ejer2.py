# Crea (si no existe) un fichero admin_log.txt 
# y añade una línea con fecha/hora (datetime) 
# y un mensaje pedido por teclado. No debe borrar el contenido anterior.
from datetime import datetime

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
m = input("Pon un mensaje: ")

with open("admin_log.txt", "a") as f:
    f.write(f"[[{fecha}]] --> {m} \n")