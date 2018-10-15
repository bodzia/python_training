# Napisz program, który będzie bazą (kontakty, samochody, itp.), program ma pytać użytkownika, co chce zrobić, dając mu minimum te opcje:
# dodanie imienia,
# usuniecie imienia,
# sprawdzenie czy imię jest w bazie,
# usunięcie imienia,
# sprawdzenie ilości imion w bazie oraz zakończenie programu.
# Jeśli czujesz się pewniej to postaraj się aby użytkownik mógł podać więcej szczegółów np. nazwisko, nr telefonu, adres itp.
# Program ten będziemy pomału rozbudowywać, w kolejnych tygodniach

import common_functions


options = ["add", "remove", "check"]
second_options = ["first_name", "last_name", "company_name", "address", "city", "county", "state", "zip", "phone1",
                  "phone", "email"]
sorted_second_options = sorted(second_options)
option = common_functions.check_input("string", "co chcesz zrobić? \nadd/remove/check")
check_option = common_functions.check_content(option, options)
second_option = common_functions.check_input("string",
                                             "first_name/last_name/company_name/address/city/county/state/zip/phone1/phone/email")
chosen_option = common_functions.check_list(second_option, ",")
chosen_option = sorted(chosen_option)
number_of_chosen_elements = len(chosen_option)

k = 0
while k < number_of_chosen_elements:
    check_second_option = common_functions.check_content(chosen_option[k], sorted_second_options)
    k += 1

number_of_elements = len(second_options)
new_line = []
element_index = 0
new_dict = {'first_name': '', 'last_name': '', 'company_name': '', 'address': '', 'city': '', 'county': '', 'state': '', 'zip': '', 'phone1': '',
                  'phone': '', 'email':''}
i = 0
j = 0
l = 1

with open('100-contacts-kopia.csv', 'a') as file:
    if option == 'add':
        for element in sorted_second_options:
            try:
                chosen_element = chosen_option[i]
            except:
                print("koniec")
            if element == chosen_element:
                value = common_functions.check_input("string", chosen_element)
                new_dict[element] = value

                i += 1
            else:
                value = "Unknown"
                new_dict[element] = value

        for second_element in second_options:
            dict_value = new_dict[second_element]
            new_line.append(dict_value)

        record = ','.join(new_line)
        print(record)
        file.seek(2)
        file.write('\n' + record)

with open('100-contacts-kopia.csv', 'r+') as file:
    if option == 'check':
        line = file.readline()
        for element in second_options:
            try:
                chosen_element = chosen_option[i]
            except:
                print("koniec")
            if element == chosen_element:
                element_index = second_options.index(chosen_element)
                value = common_functions.check_input("string", chosen_element).lower()
                while line != '':
                    current_line = common_functions.check_list(line, ",")
                    check_value = current_line[element_index].lower()
                    if value == check_value:
                        checked_value = 'T'
                    else:
                        checked_value = 'F'

                    line = file.readline()
        if checked_value == 'T':
            print("element exists")
        else:
            print("element does not exist")


    elif option == 'remove':

        all_lines = file.readlines()
        number_of_lines=len(all_lines)
        for element in second_options:

            try:
                chosen_element = chosen_option[i]
            except:
                print("koniec")
            if element == chosen_element:
                element_index = second_options.index(chosen_element)
                value = common_functions.check_input("string", chosen_element).lower()
                while j < number_of_lines:
                    current_line = common_functions.check_list(all_lines[j], ",")
                    print(current_line)
                    check_value = current_line[element_index].lower()
                    if value == check_value:
                        checked_value = 'T'
                        all_lines.remove(all_lines[j])
                        number_of_lines = number_of_lines - 1
                    else:
                        checked_value = 'F'
                    print(checked_value)
                    j += 1
                with open('100-contacts.csv', 'w') as new_file:
                    for element in all_lines:
                        new_file.write(element)
        #optional
        #import os
        #os.rename('100-contacts.csv', '100-contacts-kopia.csv')
