# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

x = input("podaj roczek: ")
a = int(x)
if a <0:
    print("to chyba nie jest roczek!")
else:
    b = a % 4
    c = a % 100
    d = a % 400


    if b == 0 and c != 0:
        print("luty będzie długi...")
    elif d == 0:
        print("luty będzie długi...")
    else:
        print("wypłata będzie szybko!")