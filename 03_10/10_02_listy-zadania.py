# 2. znajdz najwiekszy / najmniejszy element w liscie

import common_functions
elements = common_functions.check_input("list"," podaj elementy oddzielone przecineczkami: ")
number_of_elements = len(elements)
i = 0
min_value = float(elements[0])
max_value = float(elements[0])

while i < number_of_elements:
    current_element = (common_functions.check_value("float", elements[i]))

    if current_element > max_value:
        max_value = current_element
    elif current_element < min_value:
        min_value = current_element


    i += 1

print("min: ", min_value)
print("max: ", max_value)

