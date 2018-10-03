# 7. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

temp_in = input("podaj temperaturek: ")
in_length = len(temp_in)
temp_unit = str(temp_in[in_length - 1:in_length]).upper()
try:
    temp_value = int(temp_in[0:in_length - 1])
except:
    print("coś tu nie bangla!")
    exit(0)

temp_c = 0
temp_f = 0


if temp_unit == 'C':
    new_temp_unit = 'farenhajtach'
    new_temp_value = temp_value * (9/5) + 32
    new_temp_value = int(new_temp_value)
    print("temperaturek {0}{1} w {2} to {3}".format(temp_value,temp_unit,new_temp_unit,new_temp_value))
elif temp_unit == 'F':
    new_temp_unit = 'celsjuszach'
    new_temp_value = (temp_value - 32) * (5/9)
    new_temp_value = int(new_temp_value)
    print("temperaturek {0}{1} w {2} to {3}".format(temp_value,temp_unit,new_temp_unit,new_temp_value))
else:
    print("coś tu nie bangla!")
