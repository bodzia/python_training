# 5. inupt - miesiąc oraz dzien (np. mar-18),
#   okreslic pore roku

summer_months = ["jun", "jul", "aug", "sep"]
spring_months = ["mar", "apr", "may"]
autumn_months = ["oct", "nov"]
winter_months = ["dec", "jan"]

user_date = input("mon-dd: ")
month = user_date [0:3].lower()
day = int(user_date [4:6])
print(month)
print(day)
try:
    from datetime import datetime
    date_check = datetime.strptime(user_date, "%b-%d").date()
except:
    print("zła data!")

if month in winter_months:
    if month == "dec":
        if day < 22:
            print("szarooo")
        else:
            print("zimko")
    else:
        print("zimko")
elif month in autumn_months:
    print("szarooo")
elif month in summer_months:
    if month == "sep":
        if day < 23:
            print("cześć lato!")
        else:
            print("szarooo")
    elif month == "jun":
        if day < 22:
            pr
else:
    print("bla")
#day = datetime.strptime(user_date, "%d").date()
print(month)