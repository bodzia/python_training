# 1. program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1
#    cena, zaplacono, reszta
import common_functions
price = common_functions.check_input("float", "mieli_dać: ")
pay = common_functions.check_input("float", "dali: ")
#rest = 0
i = 0
rest_list = [5.0, 2.0, 1.0, 0.5, 0.2, 0.1]
rest_number = []
number_of_elements = len(rest_list)
rest = pay - price
print("reszta do wydania to: ", rest)

while i < number_of_elements:
   n = round (rest / rest_list[i],2)
   rest_decrease=str(n)[:1]
   rest_decrease=int(rest_decrease)
   rest_number.append(rest_decrease)
   rest = rest - (rest_decrease * rest_list[i])
   i += 1

print ("reszta do wydania w podziale na monety: ")

i = 0
while i < number_of_elements:
   print(rest_number[i] , " x ", rest_list[i], " zł")
   i += 1