"""
Dany jest szyfr, który zamienia samogªoski wg klucza: klucz = {”a” : ”y”, ”e” : ”i”, ”i” : ”o”, ”o” : ”a”, ”y” : ”e”}.
Czyli wszystkie a zamienia na y itd. Np. tekst: 'to jest moj tekst 'po przepuszczeniu przez szyfr to 'ta jist maj tikst'.
Napisz funkcję do szyfrowania i deszyfrowania tekstu. Przetestuj szyfrowanie i deszyfrowanie na kilku przykładach.
"""

def encrypt_txt(txt, my_key):
    output_txt = ""
    for letter in txt:
        if letter in my_key:
            output_txt += my_key[letter]
        else:
            output_txt += letter
    return output_txt

def decrypt_txt(txt, my_key):
    output_txt = ""
    for letter in txt:
        if letter in my_key.values():
            for key, val in my_key.items():
                if val == letter:
                    output_txt += key
        else:
            output_txt += letter
    return output_txt

my_key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}

input_txt_1 = "to jest moj tekst"
input_txt_2 = "aby wyruszyć w drogę, należy zebrać drużynę"
output_txt_1 = encrypt_txt(input_txt_1, my_key)
output_txt_2 = encrypt_txt(input_txt_2, my_key)

print(f"{input_txt_1} -> {output_txt_1}")
print(f"{input_txt_2} -> {output_txt_2}\n")
print(f"{output_txt_1} -> {decrypt_txt(output_txt_1, my_key)}")
print(f"{output_txt_2} -> {decrypt_txt(output_txt_2, my_key)}")
