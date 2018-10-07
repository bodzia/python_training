# 1. napisz program sumujący wszystkie elementy w liscie
import common_functions
elements = common_functions.check_input("list"," podaj elementy do dodawania oddzielone przecineczkami: ")
number_of_elements = len(elements)
i = 0
sum = 0

while i < number_of_elements:
    current_element = (common_functions.check_value("float", elements[i]))
    sum = sum + current_element
    i += 1

print(sum)
