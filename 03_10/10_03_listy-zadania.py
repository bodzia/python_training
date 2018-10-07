# 3. znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2

import common_functions
elements = common_functions.check_input("list"," podaj elementy oddzielone przecineczkami: ")
number_of_elements = len(elements)
i = 0
min_length = 2
new_list = []

while i < number_of_elements:
    current_element = (common_functions.check_value("string", elements[i]))
    length = len(current_element)

    if length >= 2:
        if current_element[0] == current_element[length-1]:
            new_list.append(current_element)

    i += 1

print("elementy to: ", new_list)

