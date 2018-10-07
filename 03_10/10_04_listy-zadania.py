# 4. program znajdujacy wartosci, ktre wystepuja tylko raz
list = [10,20,30,20,10,50,60,40,80,50,40]
number_of_elements = len(list)
i = 0
new_list = []

while i < number_of_elements:

    number_of_occurences = list.count(list[i])

    if number_of_occurences == 1:
            new_list.append(list[i])

    i += 1
print("raz występuje: ", new_list)