"""
Napisz program do kompresji i dekompresji ciągu znaków, który zawiera poniższe funkcje:
  1. compress(string), która zwraca None, gdy podany ciąg zawiera znaki inne niż litery
  lub zwraca skompresowany string wg reguły AAABBBBCAAAaaDD -> A3B4CA3a2D2
  2. decompress(string), która o dtwarza oryginalny tekst ze skompresowanego
"""

# Bartłomiej Domański

def compress(txt):
    if not txt.isalpha():
        return None

    compr_txt = ""
    count = 1

    for i in range(1, len(txt)):
        if txt[i] == txt[i - 1]:
            count += 1
        else:
            compr_txt += txt[i - 1] + (str(count) if count > 1 else "")
            count = 1

    compr_txt += txt[-1] + (str(count) if count > 1 else "")
    return compr_txt

def decompress(txt):
    decompr_txt = ""
    i = 0

    while i < len(txt):
        char = txt[i]
        i += 1
        count = ""

        # jeśli kolejny znak po char jest liczbą
        while i < len(txt) and txt[i].isdigit():
            count += txt[i]
            i += 1

        decompr_txt += char * (int(count) if count else 1)

    return decompr_txt

txt1 = "AAAAAAAAAAAAAAAAAAAA"
txt2 = "AAABBBBCAAAaaDD"
txt3 = "A213AAAAAA"
txt4 = "H12a3b2"
txt5 = "kap2a"
txt6 = "O20"

print(f"Kompresja: \n{txt1} -> {compress(txt1)}")
print(f"{txt2} -> {compress(txt2)}")
print(f"{txt3} -> {compress(txt3)}\n")

print(f"Dekompresja: \n{txt4} -> {decompress(txt4)}")
print(f"{txt5} -> {decompress(txt5)}")
print(f"{txt6} -> {decompress(txt6)}")
