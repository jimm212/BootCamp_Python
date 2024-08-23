'''Clase sobre listas'''

# Crear Lista de numeros
numeros = [1,3,5,7,8]
print(numeros)

# Crear lista de cadenas
cadena = ['manzana','plátano','pera','piña']
print(cadena)

# Crear lista Mixta
mixta = [1,'dos',3.0,[4, 5],True]
print(mixta)

# Acceder a la Lista
primer_elemento = numeros[0]
ultimo_elemento = numeros[-1]
print(primer_elemento)
print(ultimo_elemento)
print(cadena[0])

penultimo_elemento = mixta[-2]
pe_sublista = penultimo_elemento[0]  # Accede a la sublista de mixta [4 , 5] [0]
print(penultimo_elemento, pe_sublista , sep= ' , ') 

# Manipular elementos 
cadena[1] = 'mango'
print(cadena)

# Añadir elementos
cadena.append('naranja')   # al final
print(cadena)

cadena.insert(2,'guayaba') # en la posición 2
print(cadena)

# ITERAR
for element in cadena:
    print(element)
    
for i in range(3,len(cadena),2):
    print(f'Indice {i}: {cadena[i]}')
    
# ELIMINAR
cadena.remove('naranja')
print(cadena)

ultima_fruta = cadena.pop()
print(ultima_fruta)


mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
mi_lista.sort()
print(mi_lista)
mi_lista.reverse()
print(mi_lista)

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
lista_2=sorted(mi_lista)
print(lista_2)

