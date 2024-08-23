''' Evaluación  M°3 S°6 '''
#---------------------------------------------------------------------------------------
# Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y 
# entregue el orden de mayor a menor.
#---------------------------------------------------------------------------------------

num_1 = 17
num_2 = 55
num_3 = 36

if   num_1 > num_2 and num_1 > num_3:
    if num_2 > num_3:
        mayor,medio,menor = num_1,num_2,num_3
    else:
        mayor,medio,menor = num_1,num_3,num_2
elif num_2 > num_1 and num_2 > num_3:
    if num_1 > num_3:
        mayor,medio,menor = num_2,num_1,num_3
    else:
        mayor,medio,menor = num_2,num_3,num_1     
else:
    if num_1 > num_2:
        mayor,medio,menor = num_3,num_1,num_2
    else:
        mayor,medio,menor = num_3,num_2,num_1

print(f'El numero mayor es {mayor}, el medio es {medio} y el menor es {menor}')

