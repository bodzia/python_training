# 3. oblicz ocenę na podstawie progu procentowego

grade = [ 1, 2, 3, 4, 5, 6]
percentage = int(input("%%%%"))

if percentage >0 and percentage <= 30:
    print('ocenka to: ', grade[0], '!')
elif percentage >30 and percentage <= 50:
    print('ocenka to: ' , grade[1] , '!')
elif percentage >50 and percentage <= 70:
    print('ocenka to: ' , grade[2] , '!')
elif percentage >70 and percentage <= 90:
    print('ocenka to: ' , grade[3] ,'!')
elif percentage >90 and percentage < 100:
    print('ocenka to: ' , grade[4] ,'!')
elif percentage == 100:
    print('brawo, ' , grade[5] , '!')
else:
    print('%%% sie nie zgadzaja!' )
