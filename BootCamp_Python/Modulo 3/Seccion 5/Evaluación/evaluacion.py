''' Evaluación  M°3 S°5 '''
#---------------------------------------------------------------------------------------
# Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, e imprimir en 
# pantalla las consonantes restantes y su posición dentro de dicha palabra.
#---------------------------------------------------------------------------------------

palabra = 'paralelepípedo'
p_pos = []
for pos, elemento in enumerate(palabra):
    if elemento == 'a' or elemento == 'e' or elemento == 'i' or elemento == 'o' or elemento == 'u':
        continue
    else:
        p_pos.append((elemento,pos))
print(p_pos)