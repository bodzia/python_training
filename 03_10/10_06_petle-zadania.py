# 6. oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata
import common_functions
dog_age = common_functions.check_input("int", "dawaj wiek psa: ")

if dog_age >= 0 and dog_age < 3:
    human_age = dog_age * 10.5
    print("wiek człowieka: ", human_age)
elif dog_age > 2:
    young_dog = 2 * 10.5
    human_age = (dog_age-2) * 4 + young_dog
    print("wiek człowieka: ", human_age)
else:
    print("nie ma takiego wieku")