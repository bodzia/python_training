# 3. program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie
import common_functions
min = common_functions.check_input("int", "dolna granica: ")
max = common_functions.check_input("int", "gorna granica: ")

list_to_check = list(range(min, max+1))
odd_list = []
even_list = []
for element in list_to_check:
    odd = element % 2
    if odd == 0:
        odd_list.append(element)
    else:
        even_list.append(element)

odd_number = len(odd_list)
even_number = len(even_list)
print("wszystkie numerki: ", list_to_check)
print("even count: ", even_number)
print("odd count: ", odd_number)