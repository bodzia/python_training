# 6. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True
import common_functions
list_one = common_functions.check_input("list"," podaj elementy listy pierwszej oddzielone przecineczkami: ")
list_two = common_functions.check_input("list"," podaj elementy listy drugiej oddzielone przecineczkami: ")


common_elements = list(set(list_one).intersection(list_two))
number_of_common_elements = len(common_elements)

if number_of_common_elements != 0:
    print("jest część wspólna!")
else:
    print("nie ma części wspólnej!")