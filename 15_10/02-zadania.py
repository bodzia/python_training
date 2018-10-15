# przyjac od uzytkownika string
# porownac, czy string wejsciowy == string odwrocony
# jesli tak, to zwrocic true
# jesli nie, to zwrocic false

import common_functions


def string_check():
    input = common_functions.check_input("string", "dawaj stringa: ")
    revert_input = input[::-1]
    if input == revert_input:
        return True
    else:
        return False

print(string_check())

