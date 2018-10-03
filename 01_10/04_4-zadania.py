# 4. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu

months_31 = [ "styczeń","marzec", "maj", "lipiec", "sierpień", "październik", "grudzień" ]
months_30 = [ "kwiecień", "czerwiec", "wrzesień", "listopad"]
days = [28, 29, 30, 31]

month=str(input("podaj miesiąc SŁOWNIE: ")).lower()

if month in months_31:
    print("to będzie długi miesiąc...")
elif month in months_30:
    print("30 dni męki w tym miesiącu")
elif month == "luty":

    a=int(input("podaj roczek: "))

    if a < 0:
        print("to chyba nie jest roczek!")
    b = a % 4
    c = a % 100
    d = a % 400

    if b == 0 and c != 0:
        print("luty będzie długi...")
    elif d == 0:
        print("luty będzie długi...")
    else:
        print("wypłata będzie szybko!")
else:
    print("coś poszło nie tak...")