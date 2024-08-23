from math import gcd, sqrt
from typing import TypeVar

A = TypeVar('A')
B = TypeVar('B')

# ---------------------------------------------------------------------
# Ejercicio 1. Definir la función
# divisionSegura : (float, float) -> float
# tal que divisionSegura(x, y) es x/y si y no es cero y 9999 en caso
# contrario. Por ejemplo,
# divisionSegura(7, 2) == 3.5
# divisionSegura(7, 0) == 9999.0
# ---------------------------------------------------------------------

def divisionSegura(x:float, y:float) ->float:
    #if y == 0:
    #    return 9999.00
    #div = x/y
    #return div
    match y:
        case 0:
            return 9999.0
        case _:
            div = x/y
            return div

division = divisionSegura(7,0)
print(f'El resultado de la division es {division}')

# ---------------------------------------------------------------------
# Ejercicio 2. La disyunción excluyente de dos fórmulas se verifica si
# una es verdadera y la otra es falsa. Su tabla de verdad es
#   x   |   y   | xor x y
# ------+-------+---------
# True  | True  | False
# True  | False | True
# False | True  | True
# False | False | False
#
# Definir la función
# xor : (bool, bool) -> bool
# tal que xor(x, y) es la disyunción excluyente de x e y. Por ejemplo,
# xor(True, True) == False
# xor(True, False) == True
# xor(False, True) == True
# xor(False, False) == False
# ---------------------------------------------------------------------

def xor(x:bool, y:bool) -> bool:
    match x,y:
        case True, True:
            return False
        case False, False:
            return False
        case True, False:
            return True
        case False, True:
            return True
expresion =xor(True, False)
print(f'El valor logico de la expresion XOR es {expresion}')

# ---------------------------------------------------------------------
# Ejercicio 3. Las dimensiones de los rectángulos puede representarse
# por pares; por ejemplo, (5,3) representa a un rectángulo de base 5 y
# altura 3.
#
# Definir la función
# mayorRectangulo : (tuple[float, float], tuple[float, float])
# -> tuple[float, float]
# tal que mayorRectangulo(r1, r2) es el rectángulo de mayor área entre
# r1 y r2. Por ejemplo,
# mayorRectangulo((4, 6), (3, 7)) == (4, 6)
# mayorRectangulo((4, 6), (3, 8)) == (4, 6)
# mayorRectangulo((4, 6), (3, 9)) == (3, 9)
# ---------------------------------------------------------------------

def mayorRectangulo(r1: tuple[float,float],
                    r2: tuple[float,float]) -> tuple[float,float]:
    (a,b) = r1
    (c,d) = r2
    if a*b > c*d:
        return r1
    elif a*b == c*d:
        igual = r1 
        return igual
    else:
        return r2

areaRect = mayorRectangulo((4, 6), (3, 9))
print(f'El rectangulo de mayor area es {areaRect}')

# ---------------------------------------------------------------------
# Ejercicio 4. Definir la función
# intercambia : (tuple[A, B]) -> tuple[B, A]
# tal que intercambia(p) es el punto obtenido intercambiando las
# coordenadas del punto p. Por ejemplo,
# intercambia((2,5)) == (5,2)
# intercambia((5,2)) == (2,5)
#
# Comprobar con Hypothesis que la función intercambia esidempotente; es
# decir, si se aplica dos veces es lo mismo que no aplicarla ninguna.
# ---------------------------------------------------------------------

def intercambia(p: tuple[A,B]) -> tuple[B,A]:
    (x,y) = p
    return (y,x)

inter = intercambia((7,65))
print(f'El intercambio resulta en {inter}')

# ---------------------------------------------------------------------
# Ejercicio 5. Definir la función
# distancia : (tuple[float, float], tuple[float, float]) -> float
# tal que distancia(p1, p2) es la distancia entre los puntos p1 y
# p2. Por ejemplo,
# distancia((1, 2), (4, 6)) == 5.0
#
# Comprobar con Hypothesis que se verifica la propiedad triangular de
# la distancia; es decir, dados tres puntos p1, p2 y p3, la distancia
# de p1 a p3 es menor o igual que la suma de la distancia de p1 a p2 y
# la de p2 a p3.
# ---------------------------------------------------------------------

def distancia(p1: tuple[float,float],
             p2: tuple[float,float]) -> float:
    (a,b) = p1
    (c,d) = p2
    dist = sqrt((a-c)**2 + (b-d)**2)
    return dist

ds = distancia((1, 2), (4, 6))
print(f'La distancia es {ds}')

# ---------------------------------------------------------------------
# Ejercicio 6. Definir una función
# ciclo : (list[A]) -> list[A]
# tal que ciclo(xs) es la lista obtenida permutando cíclicamente los
# elementos de la lista xs, pasando el último elemento al principio de
# la lista. Por ejemplo,
#   ciclo([2, 5, 7, 9]) == [9, 2, 5, 7]
#   ciclo([])           == []
#   ciclo([2])          == [2]
#
# Comprobar que la longitud es un invariante de la función ciclo; es
# decir, la longitud de (ciclo xs) es la misma que la de xs.
# ---------------------------------------------------------------------

def ciclo(xs: list[A]) -> list[A]:
    if xs:
        cio = [xs[-1]] + xs[:-1]
        return cio
    return []

cic = ciclo([2, 5, 7, 9])
print(cic)

# ---------------------------------------------------------------------
# Ejercicio 7. Definir la función
# numeroMayor : (int, int) -> int
# tal que numeroMayor(x, y) es el mayor número de dos cifras que puede
# construirse con los dígitos x e y. Por ejemplo,
# numeroMayor(2, 5) == 52
# numeroMayor(5, 2) == 52
# ---------------------------------------------------------------------

def numeroMayor(x:int,y:int) ->int:
    return 10*max(x,y) + min(x,y)

a =  numeroMayor(5, 7)
print(a)

# ---------------------------------------------------------------------
# Ejercicio 8. Definir la función
# numeroDeRaices : (float, float, float) -> float
# tal que numeroDeRaices(a, b, c) es el número de raíces reales de la
# ecuación a*x^2 + b*x + c = 0. Por ejemplo,
# numeroDeRaices(2, 0, 3) == 0
# numeroDeRaices(4, 4, 1) == 1
# numeroDeRaices(5, 23, 12) == 2
# ---------------------------------------------------------------------

def numeroDeRaices(a:float, b:float, c:float) -> float:
    d = b**2-4*a*c
    if d > 0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0

abc = numeroDeRaices(4, 4, 1)
print(f'Numero de raices {abc}')

# ---------------------------------------------------------------------
# Ejercicio 9. Definir la función
# raices : (float, float, float) -> list[float]
# tal que raices(a, b, c) es la lista de las raíces reales de la
# ecuación ax^2 + bx + c = 0. Por ejemplo,
#   raices(1, 3, 2)    == [-1.0,-2.0]
#   raices(1, (-2), 1) == [1.0,1.0]
#   raices(1, 0, 1)    == []
#
# Comprobar con Hypothesis que la suma de las raíces de la ecuación
# ax^2 + bx + c = 0 (con a no nulo) es -b/a y su producto es c/a.
# ---------------------------------------------------------------------

def raices(a:float, b:float, c:float) -> list[float]:
    d = b**2-4*a*c
    if d >= 0:
        e = sqrt(d)
        t = 2*a
        x = (-b+e)/t
        y = (-b-e)/t
        return [x,y]
    return []

comp = raices(1, 3, 2)
print(f'Las raices se encuentran en {comp}')

# ---------------------------------------------------------------------
# Ejercicio 10. La fórmula de Herón, descubierta por Herón de
# Alejandría, dice que el área de un triángulo cuyo lados miden a, b y c
# es la raíz cuadrada de s(s-a)(s-b)(s-c) donde s es el semiperímetro
# s = (a+b+c)/2
#
# Definir la función
# area : (float, float, float) -> float
# tal que area(a, b, c) es el área del triángulo de lados a, b y c. Por
# ejemplo,
# area(3, 4, 5) == 6.0
# ---------------------------------------------------------------------

def area(a:float,b:float,c:float) -> float:
    s = (a+b+c)/2
    area_1 = s*(s-a)*(s-b)*(s-c)
    area_triang = sqrt(area_1)
    return area_triang

ar_heron =  area(3, 4, 5)
print(f'El área de un triángulo, de acuerdo a la fórmula de Herón es {ar_heron}')

# ---------------------------------------------------------------------
# Ejercicio 11. Los intervalos cerrados se pueden representar mediante
# una lista de dos números (el primero es el extremo inferior del
# intervalo y el segundo el superior).
#
# Definir la función
# interseccion : (list[float], list[float]) -> list[float]
# tal que interseccion(i1, i2) es la intersección de los intervalos i1 e
# i2. Por ejemplo,
#       interseccion([], [3, 5])     == []
#       interseccion([3, 5], [])     == []
#       interseccion([2, 4], [6, 9]) == []
#       interseccion([2, 6], [6, 9]) == [6, 6]
#       interseccion([2, 6], [0, 9]) == [2, 6]
#       interseccion([2, 6], [0, 4]) == [2, 4]
#       interseccion([4, 6], [0, 4]) == [4, 4]
#       interseccion([5, 6], [0, 4]) == []
#
# Comprobar con Hypothesis que la intersección de intervalos es
# conmutativa.
# ---------------------------------------------------------------------