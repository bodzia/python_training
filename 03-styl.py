#### import this

# Styl Python jest opisany w PEP 8

# opisowe nazwy zmiennych

print("name:")
name = input()

# x nie mowi nam nic
print("x:")
x = input()

# nie wolno zaczynac od cyfr
#1name = 34

############################################

# male litery i podkreslnik dla poprawienia czytelnosci
full_name = ''

# Camel Case - nie uzywamy, chyba, ze juz istnieje
fullName = ''

hours = 43               # unikamy komentarzy z boku
salary = 45

#------------------------

if hours < 40:
    print(hours * salary)
else:
    print((hours - (hours - 40)) * salary + (hours - 40) * (1.5 * salary))

#-----------------------

weekly_hours_worked = float(input("Worked weekly hours: "))
base_salary_per_h = float(input("Your salary per hour: "))


weekly_work_limit = 40
extratime_factor = 1.5

if weekly_hours_worked <= weekly_work_limit:
    print(weekly_hours_worked * base_salary_per_h)
else:
    # obliczamy wynagrodzenie standartowe
    base_weekly_salary = weekly_work_limit * base_salary_per_h

    # obliczamy wynagrodzenie za nadgodziny
    overtime = weekly_hours_worked - weekly_work_limit
    overtime_salary = overtime * base_salary_per_h * extratime_factor

    full_salary = base_weekly_salary + overtime_salary

    print("{}".format(full_salary))

################################################

# puste linie dla poprawienia czytelności


