''' Rebound S°3 M° 8 '''
#---------------------------------------------------------------------------------------
# En esta actividad trabajaremos con listas. Tomando la lista que se entrega a 
# continuación, se solicita realizar las siguientes acciones en el orden indicado:
#   Eliminar los elementos duplicados.
#   Ordenar la lista resultante en orden ascendente.
# La lista es:
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
#---------------------------------------------------------------------------------------
mi_lista_2 = []
for list_element in mi_lista:
    if list_element not in mi_lista_2:
        mi_lista_2.append(list_element)
print(mi_lista_2)

mi_lista_2.sort()
print(mi_lista_2)
