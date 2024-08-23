'''Ejercicio:
Imagina que estás creando una base de datos simple para una tienda de mascotas. 
Cada mascota tiene un nombre, una especie, una edad y una lista de juguetes favoritos.
Crea un diccionario donde la clave sea el nombre de la mascota y el valor sea otro 
diccionario que contenga las siguientes claves: 'especie', 'edad' y 'juguetes'.
Agrega al menos 3 mascotas a este diccionario.
Crea una función que tome como entrada el nombre de una mascota y devuelva una tupla con 
la especie y la edad.
Crea otra función que tome como entrada el nombre de un juguete y devuelva una lista con 
los nombres de todas las mascotas a las que les gusta ese juguete. Utiliza un conjunto 
intermedio para eliminar duplicados.
Crea una lista con todos los tipos de especies de mascotas en tu base de datos. Utiliza 
un conjunto para eliminar duplicados.'''

mascotas = {'Rex': {'especie': 'perro', 'edad': 5, 'juguetes': 'pelota'},
            'Gatito': {'especie': 'gato', 'edad': 2, 'juguetes': 'pelota'},
            'Mordelon': {'especie': 'hamster', 'edad': 1, 'juguetes': 'rueda'},
            'Rocky': {'especie': 'perro', 'edad': 3, 'juguetes': 'hueso'},
            'Spar': {'especie': 'gato', 'edad': 1, 'juguetes': 'pelota'},
            'Nala': {'especie': 'perro', 'edad': 0.5, 'juguetes': 'hueso'},
            'Pepe': {'especie': 'loro', 'edad': 2, 'juguetes': 'palo'}}

def mascota(x):
    for nombre in mascotas.keys():
        if x == nombre:
            salida = dict(mascotas[nombre].items())
            print(salida)
            salida = (nombre,salida['especie'],salida['edad'])
            return salida

def juguete_fav(juguete):
    lista_juguete_fav = []
    for animal in mascotas.keys():
        animal_juguete = dict(mascotas[animal].items())
        print(animal_juguete)
        if animal_juguete['juguetes'] == juguete:
            lista_juguete_fav.append(animal)
            print(lista_juguete_fav)
    return lista_juguete_fav
        
def especies_duplicadas():
    especies = []
    especies_dup = []
    for especie in mascotas.values():
        especies.append(especie['especie'])
        for element in especies:
            if element not in especies_dup:
                especies_dup.append(especie['especie'])
    return especies_dup
    
    
print(mascota('Pepe'))
print(juguete_fav('pelota'))
print(especies_duplicadas())
