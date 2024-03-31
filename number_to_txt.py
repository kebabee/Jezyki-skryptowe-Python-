"""
Napisz funkcję, która dla wprowadzonej liczby dziesiętnej (z zakresu 1-1999) wyświetli jej wartość zapisaną słownie.
"""

def num_to_txt2(num):
    if not num.isdigit():
        raise TypeError(f"{num} nie jest liczbą całkowitą.")
        
    num = int(num)
    if num < 1 or num > 1999:
        raise ValueError(f"{num} jest poza zakresem [1,1999]")
        
    num_dict = {0: 'zero', 1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery', 5: 'pięć', 6: 'sześć', 7: 'siedem',
    8: 'osiem', 9: 'dziewięć', 10: 'dziesięć', 11: 'jedenaście', 12: 'dwanaście', 13: 'trzynaście',
    14: 'czternaście', 15: 'piętnaście', 16: 'szesnaście', 17: 'siedemnaście', 18: 'osiemnaście',
    19: 'dziewiętnaście', 20: 'dwadzieścia', 30: 'trzydzieści', 40: 'czterdzieści', 50: 'pięćdziesiąt',
    60: 'sześćdziesiąt', 70: 'siedemdziesiąt', 80: 'osiemdziesiąt', 90: 'dziewięćdziesiąt', 100: 'sto',
    200: 'dwieście', 300: 'trzysta', 400: 'czterysta', 500: 'pięćset', 600: 'sześćset', 700: 'siedemset',
    800: 'osiemset', 900: 'dziewięćset', 1000: 'tysiąc'}
    output = ''

    dig1 = num % 10 # jedności
    dig2 = num % 100 - dig1 # dziesiątki
    dig3 = num % 1000 - dig2 - dig1 # setki
    dig4 = num % 10000 - dig3 - dig2 - dig1 # tysiące

    if dig4:
        output += f" {num_dict[dig4]}"
    if dig3:
        output += f" {num_dict[dig3]}"
    if dig2:
        if dig2 == 10: # czyli zakres od 10 do 19
            output += f" {num_dict[num%100]}"
            return output
        output += f" {num_dict[dig2]}"   
    if dig1:
        output += f" {num_dict[dig1]}"
    return output[1:] #eliminacja początkowej spacji

try:
    input_word = input("Podaj liczbę: ")
    res = num_to_txt2(input_word)
    print(f'{input_word} -> {res}')

except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
