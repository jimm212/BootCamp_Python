'''Eres el encargado de gestionar las calificaciones de una clase de estudiantes. 
    Tienes que implementar un pequeño programa que realice las siguientes tareas:
● Crear una lista de calificaciones: Inicializa una lista con las calificaciones 
    de los estudiantes. Asegúrate de que la lista contenga al menos 5 calificaciones, 
    que pueden ser números enteros o flotantes.
● Añadir una calificación: Permite que el usuario añada una nueva calificación a la lista.
● Eliminar una calificación: Permite que el usuario elimine una calificación 
    específica de la lista (si existe).
● Modificar una calificación: Permite que el usuario modifique una calificación 
    en una posición específica.
● Calcular el promedio: Calcula y muestra el promedio de las calificaciones.
● Mostrar las calificaciones: Imprime todas las calificaciones en la lista.'''


calificaciones  = [4.5,6.5,5.5,6.0,4.5,7.0]
print(calificaciones)
# Añadir Calificación
x = True
while x:
    sel = input('Desea añadir una calificación extra s/n -> ').lower()
    if sel == 's':
        i = True
        while i:
            try:
                add = float(input('Ingrese la nueva calificación en escala de 1 a 7 -> '))
                if add >=1 and add <= 7:
                    calificaciones.append(add)
                    i = False
                else:
                    print('Ingrese una calificación valida')
            except ValueError:
                print('Debe Ingresar un numero')
        x = False
    elif sel == 'n':
        x = False
    else:
        print('Ingrese un opción valida')
print(calificaciones)

# Eliminar Calificación
z = True
while z:
    sel = input('Desea eliminar una calificación s/n -> ').lower()
    if sel == 's':
        i = True
        while i:
            try:
                eliminar = float(input('Ingrese la calificación  a eliminar en escala de 1 a 7 -> '))
                if eliminar >=1 and eliminar <= 7:
                    for element in calificaciones:
                        if eliminar == element:
                            calificaciones.remove(element)
                            break
                        else:
                            print('No se encuentra en la lista')
                            break
                    i = False
                else:
                    print('Ingrese una calificación valida')
            except ValueError:
                print('Debe Ingresar un numero')
        z = False
    elif sel == 'n':
        z = False
    else:
        print('Ingrese un opción valida')
print(calificaciones)

# MODIFICAR Calificación
largo = len(calificaciones)
q = True
while q:
    sel = input('Desea modificar una calificación s/n -> ').lower()
    if sel == 's':
        y = True
        while y:
            try:
                entrada = int(input(f'Ingrese el indice de la calificación a modificar de 0 a {largo-1} -> '))
                if entrada in range(largo):
                    y = False
                else:
                    print(f'Ingrese un valor dentro del rango  0 a {largo-1} -> ')
            except ValueError:
                print('Ingrese un numero -> ')
        i = True
        while i:
            try:
                add = float(input('Ingrese la nueva calificación en escala de 1 a 7 -> '))
                if add >=1 and add <= 7:
                    calificaciones[entrada] = add
                    i = False
                else:
                    print('Ingrese una calificación valida')
            except ValueError:
                        print('Debe Ingresar un numero')
        q = False
    elif sel == 'n':
        q = False
    else: 
        print('Ingrese una opción valida')
print(calificaciones)

# PROMEDIO Calificación
promedio = sum(calificaciones)/len(calificaciones)
print(f'El promedio de las calificaciones es: {promedio}')

## IMPRIMIR Calificación
for element in calificaciones:
    print(element)