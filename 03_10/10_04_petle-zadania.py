# 4. program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4

list_to_be_checked = list(range(0,21))

for element in list_to_be_checked:
    number_to_remove = element % 4
    if number_to_remove == 0:
        list_to_be_checked.remove(element)

print(list_to_be_checked)