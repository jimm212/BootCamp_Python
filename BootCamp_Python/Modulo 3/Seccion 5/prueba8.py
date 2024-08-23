#Uso del AND y OR y estructuras compuestas y anidadas
nota=float(input('Introduzca su nota'))

if nota>=4 and nota<7.1:
    print('aprobado')
    resp=input('¿Juegas futbol? S/N')
    resp2=resp.upper()
    if resp2!='S' and resp2!='N':
        print('Introdujo una respuesta inválida')
    elif nota<7 and (resp2=='S'):
        print('se otorga beca de $1000')
    elif nota==7 and (resp2=='S'):  
        print('Sobresaliente, se otorga beca de $2000') 
elif nota>7:
        print('Introdujo una calificación erronea')
else:
    print('Reprobado! Estudia más')