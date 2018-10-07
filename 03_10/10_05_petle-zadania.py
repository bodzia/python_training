# 5. program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21

list_to_be_checked = list(range(0,101))
fibonacci_list = []

for element in list_to_be_checked:
    if element == 0:
        fibonacci_list.append(element)
    elif element == 1 or element == 2:
        fibonacci_list.append(1)
    elif element > 2:
        fibonacci_length =  len(fibonacci_list)
        value = fibonacci_list[fibonacci_length-1] +  fibonacci_list[fibonacci_length-2]
        if value < 101:
            fibonacci_list.append(value)

print(fibonacci_list)
