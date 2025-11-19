#Dado un nombre de archivo llamado 'backup_2025_09_03.tar.gz' extrae la fecha en formato '03-09-2025'
#(puedes extraer el año, mes y día y luego unirlos con guiones) e imprímela
#Luego cambia a '.zip' el nombre del archivo original y muéstralo.
archivo = 'backup_2025_09_03.tar.gz'

pos = archivo.find('_')
res = archivo[pos + 1:]

pos2 = res.find('_')  
año = res[: pos2]
res = res[pos2 +1:]

pos3 = res.find('_')
mes = res[: pos3]
res = res[pos3 + 1:]

pos4 = res.find('.')
dia = res[: pos4]

fecha= (dia + '-' + mes + '-' + año)

archivo_nuevo = archivo.replace('.tar.gz', '.zip')

print(f"La fecha es: {fecha}")
print(f"La cambio a .zip: {archivo_nuevo}")
