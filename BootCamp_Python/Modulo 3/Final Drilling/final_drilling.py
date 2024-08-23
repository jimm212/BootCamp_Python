'''FINAL DRILLING MODULO N°3'''
#-----------------------------------------------------------------------------------------
#Dada la siguiente lista de nombres:  
# • Harry Houdini 
# • Newton 
# • David Blaine 
# • Hawking 
# • Messi 
# • Teller 
# • Einstein  
# • Pele  
# • Juanes 
# Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, 
# Hawking y Einstein son científicos. Debemos separar los nombres en tres grupos: magos,
# científicos y otros; y escribir  una  función  llamada  hacer_grandioso(),  que  
# modifique  la  lista  de  magos añadiendo  la frase ‘El gran‘ antes del nombre de 
# cada mago.  
# Crear  una  función  llamada  imprimir_nombres(),  que  imprime  el  nombre  de  cada  
# persona  de  la lista. 
# Finalmente,  imprimir  en  pantalla  la  lista  completa  de  nombres  antes  de  ser
# modificados;  luego imprimir los nombres de los magos grandiosos, los nombres de los 
# científicos, y los restantes.
#-----------------------------------------------------------------------------------------

lista_nombres = ['Harry Houdini','Newton','David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

list_magos = []
list_cientificos = []
list_otros = []

for name in lista_nombres:
    if name in ['Harry Houdini','David Blaine','Teller']:
        list_magos.append(name)
    elif name in ['Newton','Hawking','Einstein']:
        list_cientificos.append(name)
    else:
        list_otros.append(name)

def hacer_grandioso(x):
    list_magos_grandiosos = []
    for element in x:
        list_magos_grandiosos.append(f'El gran {element}')
    return list_magos_grandiosos

def imprimir_nombres(x):
    for element in x:
        print(element)

def imprimir_pantalla(lista,magos,cientificos,otros):
    imprimir_nombres(lista)
    print(f'Los Magos Grandiosos: {hacer_grandioso(magos)}')
    print(f'Los científicos: {cientificos}')
    print(f'Los Otros: {otros}')
    
imprimir_pantalla(lista_nombres, list_magos, list_cientificos, list_otros)
