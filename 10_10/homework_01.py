# Napisz program, który będzie bazą (kontakty, samochody, itp.), program ma pytać użytkownika, co chce zrobić, dając mu minimum te opcje:
# dodanie imienia,
# usuniecie imienia,
# sprawdzenie czy imię jest w bazie,
# usunięcie imienia,
# sprawdzenie ilości imion w bazie oraz zakończenie programu.
# Jeśli czujesz się pewniej to postaraj się aby użytkownik mógł podać więcej szczegółów np. nazwisko, nr telefonu, adres itp.
# Program ten będziemy pomału rozbudowywać, w kolejnych tygodniach

import common_functions
import csv

options = ["add", "remove", "check"]
second_options = ["first_name", "last_name", "company_name", "address", "city", "county", "state", "zip", "phone1",
                  "phone", "email"]
option = common_functions.check_input("string", "co chcesz zrobić? \nadd/remove/check")
check_option = common_functions.check_content(option, options)
second_option = common_functions.check_input("string",
                                             "first_name/last_name/company_name/address/city/county/state/zip/phone1/phone/email")
check_second_option = common_functions.check_content(second_option, second_options)

chosen_option = common_functions.check_list(second_option, ",")
number_of_chosen_elements = len(chosen_option)
number_of_elements = len(second_options)
new_line = []
element_index = 0
i = 0
j = 0


with open('100-contacts-kopia.csv', 'a') as file:
    # writer = csv.writer(file, lineterminator='\n')
    if option == 'add':
        for element in second_options:
            try:
                chosen_element = chosen_option[i]
            except:
                print("koniec")
            if element == chosen_element:
                value = common_functions.check_input("string", chosen_element)
                new_line.append(value)
                i += 1
            else:
                new_line.append("Unknown")

        record = ','.join(new_line)
        # new_record = common_functions.replace_string(record,"[]'")
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
        import os

        os.rename('100-contacts.csv', '100-contacts-kopia.csv')
