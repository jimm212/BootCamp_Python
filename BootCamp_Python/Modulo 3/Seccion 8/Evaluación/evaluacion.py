''' Evaluación M° 8 '''
#---------------------------------------------------------------------------------------
#Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista 
# de listas:
lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
# Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
#   Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
#   Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.    
#   Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave
# A, la segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
#   Finalmente, imprimiremos en pantalla el diccionario resultante.
#---------------------------------------------------------------------------------------

for list_element in lista:
    if list_element[:][0] == 0:
        continue
    else:
        list_element = list_element
        for element in list_element[:]:
            if element == 0:
                list_element.remove(element)
                continue
        print(list_element)

diccionario = {
    'A' : lista[0],
    'B' : lista[1],
    'C' : lista[2],
    'D' : lista[3]
}
print(diccionario)