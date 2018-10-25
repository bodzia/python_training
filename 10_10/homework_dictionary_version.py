import common_functions
import file_processing_common_functions


options = ["add", "remove", "check"]
second_options = ["first_name", "last_name", "company_name", "address", "city", "county", "state", "zip", "phone1","phone", "email"]

option = common_functions.check_input("string", "co chcesz zrobić? \nadd/remove/check")
check_option = common_functions.check_content(option, options)

second_option = common_functions.check_input("string","first_name/last_name/company_name/address/city/county/state/zip/phone1/phone/email")

chosen_option = common_functions.check_list(second_option, ",")
chosen_option = common_functions.check_list_content(chosen_option,second_options)

file = 'test_2.csv'

if option == 'add':
    file_processing_common_functions.generate_record(chosen_option)

if option == 'remove':
        file_processing_common_functions.remove_record_by_index(file,chosen_option)

if option == 'check':
    details_available = ["count", "exists"]
    details = common_functions.check_input("string", "count/exists ")
    check_details = common_functions.check_content(details, details_available)
    search_result = file_processing_common_functions.find_record_multiple_values(file,chosen_option)
    number_of_records_matching = search_result[0]
    if details == 'count':
        print(number_of_records_matching)
    else:
        if number_of_records_matching > 0:
            print("record exists")
        else:
            print("record does not exist")

