# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

lengths = input("boczki oddzielone przecinkami: ")
try:
    lengths_list = lengths.split(",")
except:
    print ("coś poszło nie tak...")
if len(lengths_list) != 3:
    print("za mało przecinków")
    exit(0)
else:
    try:
        a = float(lengths_list[0])
        b = float(lengths_list[1])
        c = float(lengths_list[2])
    except:
        print("a gdzie numerki?")
        exit(0)

    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        print("zbudujemy trójkąt")
        if a == b == c:
            print("trójkącik będzie równoboczny")
        elif (a == b and a !=c) or (b == c and a != b):
            print("trójkącik będzie równoramienny")
        else:
            print("trójkącik będzie miał różne boczki")
    else:
        print("trójkąta nie będzie!")
        exit(0)