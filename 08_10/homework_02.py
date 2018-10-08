#stworzyć funkcję, która po otrzymaniu liczby
#całkowitej do 1 miliona zwróci wartość True jeśli ta
#liczba jest pierwsza

import common_functions

def check_number(numberek):

    check_result = ""
    result = True

    for x in range(2, numberek):
        if numberek % x == 0:
            check_result = "F"

    if numberek > 1000000:
        print("za duży numberek")
    elif check_result == "F":
        result = False
    else:
        result = True
    print(result)

check_number(common_functions.check_input("int", "numberek: "))



