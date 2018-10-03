# 5. inupt - miesiąc oraz dzien (np. mar-18),
#   okreslic pore roku

summer_months = ["jun", "jul", "aug", "sep"]
spring_months = ["mar", "apr", "may"]
autumn_months = ["oct", "nov"]
winter_months = ["dec", "jan"]

user_date = input("mon-dd: ")

length = len(user_date)

if length != 6:
    print("zła data!")
    exit(0)

else:

    try:
        from datetime import datetime
        date_check = datetime.strptime(user_date, "%b-%d").date()

    except:
        print("zła data!")
        exit(0)

    month = user_date[0:3].lower()
    day = int(user_date[4:6])

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
                print("wiosna, ach to ty!")
            else:
                print("cześć lato!")
        else:
            print("cześć lato!")
    elif month in spring_months:
        if month == "mar":
            if day < 21:
                print("zimko")
            else:
                print("wiosna, ach to ty!")
        else:
            print("wiosna, ach to ty!")
    else:
        print("coś poszło nie tak...")
        exit(0)
