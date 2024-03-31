"""
Stwórz moduł trojkat.py zawierający cztery funkcje, które na podstawie długości boków trójkąta zwracają:
  1. obwód trójkąta
  2. pole trójkąta
  3. kąty w trójkącie
  4. informację czy trójkąt jest równoboczny, równoramienny czy różnoboczny
  5. informacje czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny
Napisz program, który pobiera od użytkownika 3 liczby (długości boków trójkąta - sprawdź czy spełniony jest warunek
istnienie trójkąta) i drukuje wszystkie informacje wykorzystując funkcje z modułu trojkat.py.
"""

import triangle_mod as tr

try:
    a = input("Podaj pierwszy bok: ")
    b = input("Podaj drugi bok: ")
    c = input("Podaj trzeci bok: ")

    if not a.replace(".", "", 1).isdigit() or not b.replace(".", "", 1).isdigit() or not c.replace(".", "", 1).isdigit(): #konwersja "2.5" na "25" a potem isdigit()
        raise TypeError(f"Co najmniej jeden podany bok nie jest numeryczny.")

    s = [float(a), float(b), float(c)]

    if not (s[0] + s[1] > s[2] and s[0] + s[2] > s[1] and s[1] + s[2] > s[0]):
        raise ValueError("Podane boki nie mogą tworzyć trójkąta")

    print(f"Trójkąt {s}:")
    print(f"Pole = {tr.area(s)}")
    print(f"Obwód = {tr.circ(s)}")
    print(f"Kąty: {tr.angles(s)}")
    print(tr.sides_type(s), tr.angle_type(s))

except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)

# help(tr)
# print(dir(tr))
