"""
Napisz program, który sprawdzi, czy wprowadzone hasło spełnia poniższe wymagania: 
Write a Python program to check the validity of password input by users. Go to the editor Validation : import re
  1. Zawiera co najmniej 1 literę alfabetu [a-z] oraz [A-Z].
  2. Zawiera co najmniej 1 liczb z przedziału [0-9].
  3. Zawiera co najmniej 1 znak specjalny ze zbioru [$#@].
  4. Długość hasła jest nie mniejsza niż 6 znaków i nie dłuższa niż 16 znaków.
"""

import re

def password_test(txt):
    if not re.search("[A-Z]", txt):
        return False

    if not re.search("[a-z]", txt):
        return False

    if not re.search("[0-9]", txt):
        return False

    if not re.search("[$#@]", txt):
        return False

    if len(txt) < 17 and len(txt) > 5:
        return True
    
    return False

def set_password():
    count = 0
    txt = input("Wymagana co najmniej jedna mała litera, duża litera, cyfra i znak z $#@, długość od 6 do 16 znaków.\nPodaj nowe hasło:\n")
    a = password_test(txt)

    while (a == False):
        count += 1
        if count == 10:
            break
        txt = input(f"Hasło nie spełnia wymagań, pozostało {10 - count} prób.\n")
        a = password_test(txt)
    if count == 10:
        print("Przekroczono liczbę prób.")
        return None
    else:
        print("Hasło zaktualizowane poprawnie.")
        return txt

password = set_password()
print(password)
