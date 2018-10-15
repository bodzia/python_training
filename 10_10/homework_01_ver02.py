# Napisz program, który będzie bazą (kontakty, samochody, itp.), program ma pytać użytkownika, co chce zrobić, dając mu minimum te opcje:
# dodanie imienia,
# usuniecie imienia,
# sprawdzenie czy imię jest w bazie,
# usunięcie imienia,
# sprawdzenie ilości imion w bazie oraz zakończenie programu.
# Jeśli czujesz się pewniej to postaraj się aby użytkownik mógł podać więcej szczegółów np. nazwisko, nr telefonu, adres itp.
# Program ten będziemy pomału rozbudowywać, w kolejnych tygodniach

import common_functions

dict = {'first_name': '', 'last_name': '', 'company_name': '', 'address': '', 'city': '', 'county': '', 'state': '', 'zip': '', 'phone1': '','phone': '', 'email':''}
second_options = ["first_name", "last_name", "company_name", "address", "city", "county", "state", "zip", "phone1",
                    "phone", "email"]
options = ["add", "remove", "check"]
option = common_functions.check_input("string", "co chcesz zrobić? \nadd/remove/check")
check_option = common_functions.check_content(option, options)
second_option = common_functions.check_input("string",
                                          "first_name/last_name/company_name/address/city/county/state/zip/phone1/phone/email")
chosen_option = common_functions.check_list(second_option, ",")


i = 0
new_line = []
new_dict = {}
number_of_chosen_elements = len(chosen_option)

k = 0
while k < number_of_chosen_elements:
    check_second_option = common_functions.check_content(chosen_option[k], second_options)
    k += 1

with open('100-contacts-kopia.csv', 'r+') as file:
    line = file.readline()
    while line != '':
            for element in second_options:
                element_index = second_options.index(element)
                try:
                    current_line = common_functions.check_list(line, ",")
                    value = current_line[element_index].lower()
                    dict[element] = value
                    line = file.readline()
                except:
                    print("not enough values")
                    line = file.readline()
            print(dict)
    if option == 'add':
            try:
                chosen_element = chosen_option[i]
            except:
                print("koniec")
            for element in second_options:
                try:
                    chosen_element = chosen_option[i]
                except:
                    print("koniec")
                if element == chosen_element:
                    value = common_functions.check_input("string", chosen_element)
                    i += 1
                else:
                    value = "Unknown"
                dict[element] = value
                for second_element in second_option:
                    new_line.append(dict[second_element])
            record = ','.join(new_line)
            file.readlines()
            file.write('\n' + record)
    if option == 'check':
            while i < number_of_chosen_elements:
               value = common_functions.check_input("string", chosen_option[i]).lower()
               new_dict[chosen_option[i]] = value
               i += 1
            exist = True
            for key in new_dict:
                for element in dict:
                    print(element)
                    print(dict[key])
                    print(new_dict[key])
                    print(dict[key])
                    if new_dict[key] == dict[key]:
                        pass
                    else:
                        exist = False
            if exist is True:
                print("element exists")
            else:
                print("element does not exist")




























#
# number_of_elements = len(second_options)
#
# element_index = 0
# new_dict = {'first_name': '', 'last_name': '', 'company_name': '', 'address': '', 'city': '', 'county': '', 'state': '', 'zip': '', 'phone1': '',
#                   'phone': '', 'email':''}
# i = 0
# j = 0
# l = 1
#
# with open('100-contacts-kopia.csv', 'a') as file:
#     if option == 'add':
#         for element in sorted_second_options:
#             try:
#                 chosen_element = chosen_option[i]
#             except:
#                 print("koniec")
#             if element == chosen_element:
#                 value = common_functions.check_input("string", chosen_element)
#                 new_dict[element] = value
#
#                 i += 1
#             else:
#                 value = "Unknown"
#                 new_dict[element] = value
#
#         for second_element in second_options:
#             dict_value = new_dict[second_element]
#             new_line.append(dict_value)
#
#         record = ','.join(new_line)
#         print(record)
#         file.seek(2)
#         file.write('\n' + record)
#
# with open('100-contacts-kopia.csv', 'r+') as file:
#     if option == 'check':
#         line = file.readline()
#         for element in second_options:
#             try:
#                 chosen_element = chosen_option[i]
#             except:
#                 print("koniec")
#             if element == chosen_element:
#                 element_index = second_options.index(chosen_element)
#                 value = common_functions.check_input("string", chosen_element).lower()
#                 while line != '':
#                     current_line = common_functions.check_list(line, ",")
#                     check_value = current_line[element_index].lower()
#                     if value == check_value:
#                         checked_value = 'T'
#                     else:
#                         checked_value = 'F'
#
#                     line = file.readline()
#         if checked_value == 'T':
#             print("element exists")
#         else:
#             print("element does not exist")
#
#
#     elif option == 'remove':
#
#         all_lines = file.readlines()
#         number_of_lines=len(all_lines)
#         for element in second_options:
#
#             try:
#                 chosen_element = chosen_option[i]
#             except:
#                 print("koniec")
#             if element == chosen_element:
#                 element_index = second_options.index(chosen_element)
#                 value = common_functions.check_input("string", chosen_element).lower()
#                 while j < number_of_lines:
#                     current_line = common_functions.check_list(all_lines[j], ",")
#                     print(current_line)
#                     check_value = current_line[element_index].lower()
#                     if value == check_value:
#                         checked_value = 'T'
#                         all_lines.remove(all_lines[j])
#                         number_of_lines = number_of_lines - 1
#                     else:
#                         checked_value = 'F'
#                     print(checked_value)
#                     j += 1
#                 with open('100-contacts.csv', 'w') as new_file:
#                     for element in all_lines:
#                         new_file.write(element)
#         #optional
#         #import os
#         #os.rename('100-contacts.csv', '100-contacts-kopia.csv')
