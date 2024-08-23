''' Evaluación  M°3 S°7 '''
#---------------------------------------------------------------------------------------
# Dada una lista de diccionarios que representan información de estudiantes, realiza 
# las siguientes tareas:
estudiantes = [
    {'nombre': 'Juan' , 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana'  , 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis' , 'edad': 20, 'calificaciones': [88, 85, 92]},
]
#Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:  
#   Filtra y muestra únicamente los estudiantes que tienen más de 18 años y cuyo 
#       promedio de calificaciones sea superior a 85. 
#   Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 
#       años y cuya edad sea un número primo. 
#---------------------------------------------------------------------------------------
estudiantes_f1 = []
for estudiante in estudiantes:
    if estudiante['edad'] > 18:
        promedio = sum(estudiante['calificaciones'])/len(estudiante['calificaciones'])
        if promedio > 85:
            estudiantes_f1.append(estudiante)

estudiantes_f2 = []         
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and estudiante['edad'] in [2,3,5,7,11,13,17,19,23]:
        estudiantes_f2.append(estudiante)

print(estudiantes_f1)
print(estudiantes_f2)
