with open('test_file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    #print(lines)
    for line in lines:
        print(line, end='')