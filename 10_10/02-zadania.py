with open('test_file.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    print(line, end='')
    print(file.readline())
