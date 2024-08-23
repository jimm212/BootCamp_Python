"""Ejercicio: Listas y Diccionarios"""
"""Gestión de proyectos: Estás desarrollando un sistema para gestionar proyectos 
de software en una empresa. Cada proyecto debe estar representado por un diccionario
que contiene la siguiente información:

-El nombre del proyecto.
-El estado actual del proyecto (por ejemplo, "En desarrollo", "Completado", "En espera").
-El presupuesto asignado al proyecto.
-equipo (dict): Un diccionario que representa el equipo de desarrolladores, con roles
como "Frontend", "Backend", "DBA", y los nombres de los responsables.
-etapas (list): Una lista de las etapas del proyecto (por ejemplo, "Diseño", "Desarrollo",
"Pruebas").

Se te pide realizar las siguientes tareas con interactividad desde el teclado:

Añadir un nuevo proyecto a la lista: Solicita al usuario que ingrese los datos del 
proyecto (nombre, estado, presupuesto, equipo, etapas) y agrégalos a la lista de proyectos.

Actualizar el estado de un proyecto existente: Permite que el usuario actualice el estado 
de un proyecto ingresando su nombre.

Calcular el presupuesto total de todos los proyectos: Suma los presupuestos de todos los 
proyectos y muestra el total al usuario.

Listar los nombres de todos los desarrolladores en un proyecto específico: Muestra los 
nombres de los desarrolladores de un proyecto ingresado por el usuario.

Eliminar un proyecto de la lista por su nombre: Elimina un proyecto de la lista ingresando
su nombre.

Mostrar la lista completa de proyectos: Muestra todos los proyectos junto con sus detalles.

El programa debe presentar un menú interactivo que permita al usuario seleccionar cada 
una de las acciones descritas."""

# Lista que contiene proyectos y otros datos adicionales.
proyectos = []

# 1. Añadir un nuevo proyecto
def agregar_proyecto():
    nombre = input("Ingresa el nombre del proyecto: ")
    estado = input("Ingresa el estado del proyecto (por ejemplo, 'En desarrollo', 'Completado', 'En espera'): ")
    presupuesto = int(input("Ingresa el presupuesto del proyecto: "))
    
    equipo = {}
    while True:
        rol = input("Ingresa el rol del equipo (por ejemplo, 'Frontend', 'Backend') o 'fin' para terminar: ")
        if rol.lower() == 'fin':
            break
        miembro = input(f"Ingresa el nombre del {rol}: ")
        equipo[rol] = miembro
    
    etapas = []
    while True:
        etapa = input("Ingresa una etapa del proyecto (por ejemplo, 'Diseño', 'Desarrollo') o 'fin' para terminar: ")
        if etapa.lower() == 'fin':
            break
        etapas.append(etapa)
    
    nuevo_proyecto = {
        "nombre": nombre,
        "estado": estado,
        "presupuesto": presupuesto,
        "equipo": equipo,
        "etapas": etapas
    }
    proyectos.append(nuevo_proyecto)

# 2. Actualizar el estado de un proyecto
def actualizar_estado_proyecto():
    nombre = input("Ingresa el nombre del proyecto que deseas actualizar: ")
    nuevo_estado = input("Ingresa el nuevo estado: ")
    for proyecto in proyectos:
        if proyecto["nombre"] == nombre:
            proyecto["estado"] = nuevo_estado
            print(f"Estado del proyecto '{nombre}' actualizado a '{nuevo_estado}'.")
            return
    print(f"Proyecto con nombre '{nombre}' no encontrado.")

# 3. Calcular el presupuesto total de todos los proyectos
def calcular_presupuesto_total():
    total = sum(proyecto["presupuesto"] for proyecto in proyectos)
    print(f"El presupuesto total de todos los proyectos es: {total}")

# 4. Listar los nombres de todos los desarrolladores en un proyecto específico
def listar_desarrolladores():
    nombre_proyecto = input("Ingresa el nombre del proyecto: ")
    for proyecto in proyectos:
        if proyecto["nombre"] == nombre_proyecto:
            desarrolladores = list(proyecto["equipo"].values())
            print(f"Desarrolladores en el proyecto '{nombre_proyecto}': {desarrolladores}")
            return
    print(f"Proyecto con nombre '{nombre_proyecto}' no encontrado.")

# 5. Eliminar un proyecto por nombre
def eliminar_proyecto():
    nombre = input("Ingresa el nombre del proyecto que deseas eliminar: ")
    for proyecto in proyectos:
        if proyecto["nombre"] == nombre:
            proyectos.remove(proyecto)
            print(f"Proyecto '{nombre}' eliminado.")
            return
    print(f"Proyecto con nombre '{nombre}' no encontrado.")

# Menú interactivo
def menu():
    while True:
        print("\nGestión de Proyectos de Software")
        print("1. Añadir un nuevo proyecto")
        print("2. Actualizar el estado de un proyecto")
        print("3. Calcular el presupuesto total de todos los proyectos")
        print("4. Listar los desarrolladores en un proyecto")
        print("5. Eliminar un proyecto")
        print("6. Mostrar todos los proyectos")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            agregar_proyecto()
        elif opcion == '2':
            actualizar_estado_proyecto()
        elif opcion == '3':
            calcular_presupuesto_total()
        elif opcion == '4':
            listar_desarrolladores()
        elif opcion == '5':
            eliminar_proyecto()
        elif opcion == '6':
            print("Proyectos actuales:", proyectos)
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar menú
menu()