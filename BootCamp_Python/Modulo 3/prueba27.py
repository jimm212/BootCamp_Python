"""Conversión de estructuras de datos"""

#Convertir una Lista en un diccionario
#Forma 1:Lista de tuplas(clave,valor)

lista_tuplas=[('nombre','Juan'),('edad',30),('ciudad','Caracas')]
diccionario=dict(lista_tuplas)
print(diccionario)

#Forma 2:Lista de listas con dos elementos
lista_listas=[['nombre','Ana'],['edad',25],['ciudad','Santiago'],['ciudad','Concepción']]
diccionario=dict(lista_listas)
print("clave repetida",diccionario)

#Forma 3:Lista de elementos pares
lista=['nombre','Pedro','edad',40,'ciudad','Trujillo']
diccionario={}
for i in range(0,len(lista),2):
    diccionario[lista[i]]=lista[i+1]
print(diccionario)

#Convertir Diccionario en Lista
diccionario={'nombre':'Maria','edad':28,'ciudad':'Concepción'}

#Crear lista de tuplas(clave,valor)
lista_tuplas=list(diccionario.items())
print(f'lista de tuplas: {lista_tuplas}')

#Crear lista de listas con dos elementos
lista_listas=[[clave,valor] for clave, valor in diccionario.items()]
print(lista_listas)

#Tarea: Obtener esta salida ['nombre','Maria','edad',28,'ciudad','Concepción'] partiendo del diccionario

#Combinar dos listas en un diccionario
nombres=['Ana','Juan','Maria']
edades=[30,25,40]

#Combinamos las listas usando zip()
pares=zip(nombres,edades)

diccionario=dict(pares)
print(dict)

#Combinando más de dos listas
frutas=['manzana','naranja','limon']
colores=['rojo','anaranjada','verde']
precios=[1.5,0.8,2.0]


frutas_info=dict(zip(frutas,zip(colores,precios)))
print(frutas_info)
#salida:{'manzana':('rojo',1.5),.....}

print(f"El color de la manzana es: {frutas_info['manzana'][0]} y el precio del limón es: {frutas_info['limon'][1]}")
