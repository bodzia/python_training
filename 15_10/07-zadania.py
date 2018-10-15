path = "c:\\moj_plik.txt"
try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print("incorrect path")
except AssertionError:
    pass
except Exception:
    print("unknown error")

print("the end")