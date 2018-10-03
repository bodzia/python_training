# 1. czy liczba jest podzielna przez 3 lub 5 lub 7
x = input("podaj numerek: ")
a = float(x)
if a < 0:
    print("zły numerek!")
else:
    e, f, g = 3, 5, 7
    b = a % e
    c = a % f
    d = a % g

    if b == 0 :
         print('szach mat, działa i dzieli się przez ' , e , '!')
    elif c == 0:
         print('szach mat, działa i dzieli się przez ' , f , '!')
    elif d == 0:
         print('szach mat, działa i dzieli się przez ' , g , '!')
    else:
        print('zonk, próbuj dalej')
