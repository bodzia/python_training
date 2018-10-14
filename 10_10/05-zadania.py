with open('test_file.txt', 'r', encoding='utf-8') as file:
    text = file.read(3)
    print(text)
    print(file.readline())
    position = file.tell()
    print("current_position {}".format(position))

    file.seek(0)
    new_position = file.tell()
    print("current_position {}".format(new_position))
