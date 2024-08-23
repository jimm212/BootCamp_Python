#TAREA hacer lista simple desde diccionario: ['nombre','maria','edad',28,'ciudad','concepcion']
 
diccionario={'nombre':'maria','edad':28,'ciudad':'concepcion'}
 
lista_simple=[]
 
for clave,valor in diccionario.items():
    lista_simple.append(clave)
    lista_simple.append(valor)
print(lista_simple)