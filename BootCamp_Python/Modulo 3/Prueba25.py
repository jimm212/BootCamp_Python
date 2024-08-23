# Tupla Vacia
tupla_vacia = ()
# Tupla varios Elementos
tupla_elementos  = (1,2,3,"Python",4.5, 2, 'Python',2)

# Tupla_emelentos_unico
tupla_emelentos_unico = (5,)

# Acceso al primer elemento
print(tupla_elementos[0])
# Acceso al ultimo elemento
print(tupla_elementos[-1])

# Contar cuantas veces aparece un elementos en la tupla
print(tupla_elementos.count('Python'))
# Encontrar el indice
print(tupla_elementos.index(2))

# Recorrido tupla
for elemento in tupla_elementos:
    print(elemento)
    
# Desempaquetado
tupla = (1,2,3)
a,b,c = tupla
print(f'Primer  elemento: {a}')
print(f'Segundo elemento: {b}')
print(f'Tercer  elemento: {c}')

lista = [1,2,3,4]
x,y,z,k = lista
print(x)

diccionario = {'uno':1,'dos':2,'tres':'3'}
d1,d2,d3 = diccionario
print(f'El primer valor del dic.. es {d1}')

(d1,v1),(d2,v2),(d3,v3) = diccionario.items()
print(f'Segundo elemento de dicc... su clave {d2}, su valor {v2}')