mi_dicionario = {
    'nombre': 'Juan',
    'edad': 30,
    'Ocupacion': 'ingeniero'    
}

nueva_clave = input('Introduzca la nueva clave: ')
nuevo_valor = input('Introduzca el nuevo valor: ')

mi_dicionario[nueva_clave] = nuevo_valor
mi_dicionario['Apellido'] = 'Perez'

print (mi_dicionario)
edad = mi_dicionario.pop('edad')
# del mi_dicionario['edad'] # Este método no guarda nada.
print (mi_dicionario)


nombre    = mi_dicionario['nombre']
#edad      = mi_dicionario['edad']
profesion = mi_dicionario.get('ocupacion')

claves = mi_dicionario.keys()
print(claves)
valor =  mi_dicionario.values()
print(valor)
items = mi_dicionario.items()
print(items)

direccion = mi_dicionario.get('direccion', 'No especificada')

print(f'El nombre es: {nombre} y su edad es: {edad}, ejerce como {profesion}')
print(f'vive en: {direccion}')

diccionario_copia = mi_dicionario.copy()
print(diccionario_copia)
mi_dicionario.clear()
print(mi_dicionario)

cant1 = len(mi_dicionario)
cant2 = len(diccionario_copia)

print(cant1,cant2, sep=' , ')

## Get se usa en caso que no se tenga la certeza de si el elemento que buscamos existe
## Lo que ocurre si el diccionario con el que se trabaja no es nuestro 