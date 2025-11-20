#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.
practica1= float(input("En la primera práctica saque un: "))
practica2= float(input("En la segunda práctica saque un: "))
practica3= float(input("En la tercera práctica saque un: "))

examen_final= float(input("En el examen final saque un: "))

trabajo_final= float(input("En el trabajo final saque un: "))

practica_final= (practica1 + practica2 + practica3)/3
practica_final2= round(practica_final, 2)
nota=(practica_final * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)/3
nota2= round(nota, 2)
print("La nota media de las prácticas es de: " ,practica_final2)
print("La nota media del curso es de: ", nota2)