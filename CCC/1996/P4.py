def numeral_to_number(numeral:str) -> int:
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0

    for i in range(len(numeral)):
        if r[numeral[i-1]] < r[numeral[i]] and i > 0:
            number += r[numeral[i]] - r[numeral[i-1]]*2
        else:
            number += r[numeral[i]]
    
    return number


def number_to_numeral(number:int) -> str:
    r = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    numeral = ""

    for i in r.keys():
        while number >= i:
            numeral += r[i]
            number -= i
       
    return numeral
    

for i in range(int(input())):
    e = input().removesuffix("=")
    e1,e2 = e.split("+")
    r = numeral_to_number(e1)+numeral_to_number(e2)
    print(f"{e}={number_to_numeral(r)}" if r <= 1000 else f"{e}=CONCORDIA CUM VERITATE")