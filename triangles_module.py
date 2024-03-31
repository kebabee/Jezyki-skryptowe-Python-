""" Moduł do kodu triangles.py, tu powninien być jakiś ładny tekst o działaniu funkcji."""
import numpy as np

def circ(sides):
    return np.sum(sides)

def area(sides):
    p = 1/2 * circ(sides)
    return np.sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))

def sides_type(sides):
    if sides[0] == sides[1] == sides[2]:
        return "równoboczny"
    elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return "równoramienny"
    else:
        return "różnoboczny"

def angle_type(sides):
    a2 = sides[0]**2
    b2 = sides[1]**2
    c2 = sides[2]**2
    if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        return "prostokątny"
    elif a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2:
            return "ostrokątny"
    else:
        return "rozwartokątny"
    
def angles(sides): # zwraca kąty wewnętrzne
    ar = area(sides)
    # P = 1/2 a b sin(alpha) -> alpha = arcsin(2P/ab)
    a1 = np.degrees(np.arcsin(2 * ar / (sides[0] * sides[1])))
    a2 = np.degrees(np.arcsin(2 * ar / (sides[1] * sides[2])))
    a3 = np.degrees(np.arcsin(2 * ar / (sides[0] * sides[2])))
    return [a1, a2, a3]
