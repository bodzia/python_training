import os
path = "c:\\moj_plik.txt"

if os.path.exists(path):
    with open(path) as file:
        print(file.read())

else:
    print("file not exists")
print("the end")


login = 'pythonisagdansk'