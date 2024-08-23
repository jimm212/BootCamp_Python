#Crear conjunto vacío
conjunto_vacio=set()

#Crear conjunto con elementos
conjunto={1,2,3,4,5}
print(conjunto)

conjunto_cadenas={"Hola","Luis","Ingeniero"}
print(conjunto_cadenas)

conjunto_duplicado={1,2,2,3,4,4}
print(conjunto_duplicado)

#Añadir elemento
conjunto.add(8)
print(conjunto)

#eliminar elemento
conjunto_cadenas.remove("Luis")
print(conjunto_cadenas)

#conjunto_cadenas.remove("Luis") #con este método no elimino el elemento no existente (obviamente),pero genera un error
conjunto_cadenas.discard("Luis") #con este método no elimino el elemento no existente (obviamente),pero NO genera un error

elemento_devuelto=conjunto.pop()
print(elemento_devuelto)
print(conjunto)

#Eliminar todos los elementos
conjunto.clear()
print(conjunto)

conjunto_a={"Ana","Lucia","Maria","Veronica"}
cadena=input("Introduce el valor a buscar")

for nombre in conjunto_a:
    if cadena==nombre:
        print("Eureka!")
        
if cadena in conjunto_a:
    print("Eureka!")

curso_a={"Ana","Lucia","Maria","Veronica"}
curso_b={"Lucia","Javier","Maria","Miguel","Jose"}
curso_c={"Pedro","Javier","Maria","Edgar","Jose"}

#Estudiantes en ambos cursos
ambos_cursos=curso_a.intersection(curso_b)
print(ambos_cursos)

resultado=curso_a.intersection(curso_b).intersection(curso_c)
print(resultado)

resultado=curso_a & curso_b & curso_c
print(resultado)

#reduce pertenece a functools

#Estudiantes solo en curso A
solo_a=curso_a.difference(curso_b)
print(solo_a)

#Estudiantes solo en curso B
solo_b=curso_b.difference(curso_a)
print(solo_b)

todos=curso_a.union(curso_b).union(curso_c)
print(todos)
todos= curso_a | (curso_b) | (curso_c)
print(todos)