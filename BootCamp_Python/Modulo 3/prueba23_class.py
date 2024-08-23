"""Clase sobre Listas"""

#Crear lista de numeros
vacia=[]
numeros=[1,3,5,7,8]
print(numeros)

#Crear lista de cadenas
frutas=['manzana',"platano","pera","piña"]
print(frutas)

#Lista mixta
mixta=[1,"dos",3.0,[4,5],True]
print(mixta)

#Acceder a lista
primer_lemento=numeros[0]
print(primer_lemento)

elemento_fruta=frutas[2]
print(elemento_fruta)

ultimo_numeros=numeros[4]
print(ultimo_numeros)

ultimo_frutas=frutas[-1]
print(ultimo_frutas)

penultimo_mixta=mixta[-2]
print(penultimo_mixta)

pe_sublista=penultimo_mixta[0]
print(pe_sublista)

#Modificación de elementos
numeros[3]=10
print(numeros)

frutas[1]='mango'
print(frutas)

#Agregar elementos
frutas.append("naranja")
print(frutas)

frutas.append("naranja")

frutas.insert(2,"guayaba")
print(frutas)

#Recorrer listas por elemento
for fruta in frutas:
    print(fruta)

#Recorrer listas usando indices
for i in range(3,len(frutas),2):
    print(f'Índice {i}: {frutas[i]}')

#Eliminar elementos
frutas.remove("mango")
print(frutas)

frutas.remove("naranja")
print(frutas)

ultima_fruta=frutas.pop()
print(frutas)

frutas.append('manzana')


lista=[1,1,1,2,1,1,2,3,3,4,5,6,1,1,2,2,3]
print(lista)

if 1 in lista:
    print('Esta presente')
    
lista2=sorted(lista)
print("lista2= ",lista2)
print("lista (desordenada)= ",lista)

lista.sort()
print("lista (ordenada)= ",lista)

lista3=list(reversed(lista))
print(lista3)

lista.reverse()
print(lista)



    
#Obtener indice
indice=frutas.index("pera")
print(indice)

#Crear lista tama;o específico
lista_vacia=[None]*10
print(lista_vacia)

#Crear sublistas
sublista_frutas=frutas[:len(frutas)//2]
print(sublista_frutas)

frutas.append('kiwi')
print(frutas)
sublista_frutas=frutas[:len(frutas)//4]
print(sublista_frutas)



