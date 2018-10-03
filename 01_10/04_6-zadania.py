# 6. ruletka: otrzymawszy liczbę, sprawdź czy jest ona (np. 17R, 2B):
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

data_in = input("numberek:")
in_length = len(data_in)
if in_length > 3:
    print("nie ma grania1!")
    exit(0)
else:
    color = data_in[in_length - 1:in_length]
    color = str(color).upper()
    number = data_in[0:in_length - 1]

    try:
        number = int(number)
    except:
        print("nie ma takiego numerku")
        exit(0)


    if color == "B":
        print("czarność")
    elif color == "R":
        print("czerwoność")
    else:
        print("nie ma takiego kolorku!")
        exit(0)
    if number > 0 and number <= 18:
        print("słabiutkooo")
    elif number > 18 and number <= 36:
        print("wysokoooo")
    else:
        print("nie ma takiego numeru!")
        exit(0)
    even_num = number % 2
    if even_num == 0:
        print("dzieli sie!")
    else:
        print("nie dzieli sie!")
