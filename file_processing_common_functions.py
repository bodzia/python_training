from copy import copy
import common_functions


dict_keys = ["first_name", "last_name", "company_name", "address", "city", "county", "state", "zip", "phone1", "phone",
             "email"]


def add_record(filename, record):
    with open(filename, 'r+') as file:
        file.readlines()
        file.write(record + '\n')


def get_all_records(filename):
    all_dict = []
    dict = {}
    with open(filename, 'r') as file:
        line = file.readline()
        while line != '':
            try:
                current_line = common_functions.check_list(line, ",")
            except:
                print("not enough values")
            for key, value in zip(dict_keys, current_line):
                dict[key] = value.rstrip('\n')
            all_dict.append(copy(dict))
            line = file.readline()
        return all_dict


def find_record_value(filename, key, value, mode='remove'):
    i = 0
    all_records = get_all_records(filename)
    result = next((item for item in all_records if item[key] == value), False)
    if result != False:
        print("record exists")
        i += 1
    else:
        print("record does not exist")
    if mode == 'remove':
        return result
    else:
        return i


def find_record_key(filename, key, result='number'):
    records = []
    all_records = get_all_records(filename)
    for record in all_records:
        value = record.get(key)
        records.append(value)
    for value in records:
        number_of_occurences = records.count(value)
        if number_of_occurences > 1:
            records.remove(value)
    if result == 'list':
        return records
    else:
        return len(records)


def remove_record(filename, key, value):
    all_records = get_all_records(filename)
    record_to_be_removed = find_record_value(filename, key, value)
    if record_to_be_removed != False:
        all_records.remove(record_to_be_removed)
    else:
        print("record does not exist")
    return all_records


def export_dictionary_to_file(filename, dict):
    # full_line = []
    with open(filename, 'r+') as file:
        for record in dict:
            full_line = []
            for key in dict_keys:
                current_line = record.get(key)
                full_line.append(current_line)
                line_to_write = ','.join(full_line)
            add_record(filename, line_to_write)


def generate_record(option_list):
    output = []
    record = dict.fromkeys(dict_keys, "Unknown")
    for element in option_list:
        value = common_functions.check_input("string", element)
        record[element] = value
    output.append(record)
    export_dictionary_to_file('test_2.csv', output)



def count_records_key(filename, key):
    print(find_record_key(filename, key))


def count_records_value(filename, key, value):
    all_records = get_all_records(filename)
    i = 0
    for record in all_records:
        if record[key] == value:
            i += 1
        else:
            pass
    return i

def create_dictionary(key_list,mode = 'filename'):
    output = []
    dictionary = dict.fromkeys(key_list)
    for element in key_list:
        if mode == 'filename':
            value = record.get(element)
        dictionary[element] = value
    output.append(dictionary)

def create_dictionary_input(option_list):
    output = []
    dictionary = dict.fromkeys(option_list)
    for element in option_list:
        value = common_functions.check_input("string", element)
        dictionary[element] = value
    output.append(dictionary)
    return dictionary

def create_dictionary_file(filename,option_list):
    output = []
    all_records = get_all_records(filename)
    dictionary = dict.fromkeys(option_list)
    for record in all_records:
        for element in option_list:
            value = record.get(element)
            dictionary[element] = value
        output.append(copy(dictionary))
    return output

def create_dictionary_to_export(all_records):
    output = []
    dictionary = dict.fromkeys(dict_keys)
    for record in all_records:
        for element in dict_keys:
            value = record.get(element)
            dictionary[element] = value
        output.append(copy(dictionary))
    return output

def create_expected_dictionary (options):
    expected_values = create_dictionary_input(options)
    expected_values = dict(expected_values)
    return expected_values

def find_record_multiple_values(filename, options):
    full_dictionary = get_all_records(filename)
    expected_values = create_expected_dictionary(options)
    number_of_keys = len(expected_values.keys())
    number_of_occurences = 0
    index = []
    for element in full_dictionary:
        i = 0
        for key,value in expected_values.items():
            if element[key].lower() == value.lower():
                i += 1
            if i == number_of_keys:
                number_of_occurences += 1
                index = [i for i, x in enumerate(full_dictionary) if x == element]
                #index.append(current_index)
    return [number_of_occurences,index]


# def get_index_value(filename,options):
#     full_dictionary = get_all_records(filename)
#     expected_values = create_dictionary_input(options)
#     expected_values = dict(expected_values)
#     number_of_keys = len(expected_values.keys())
#     number_of_occurences = 0
#     for element in full_dictionary:
#         i = 0
#         for key, value in expected_values.items():
#             if element[key] == value:
#                 index = full_dictionary.index(result)
#                 return index
#                 i += 1
#             else:
#                 print("can't find")

def remove_record_by_index(filename,options):
    all_records = get_all_records(filename)
    search_result = find_record_multiple_values(filename,options)
    if  search_result[0] > 0:
        indexes = search_result[1]
        number_of_records = len(indexes)
        i = 0
        while i < number_of_records:
            index = int(indexes[i])
            record_to_be_removed = all_records[index - i]
            all_records.remove(record_to_be_removed)
            i+=1
        print ("success")
        new_database = create_dictionary_to_export(all_records)
        export_dictionary_to_file('test_remove.csv', new_database)
    else:
        print("no record to delete")


#print(get_index_value('test_2.csv',["first_name","last_name"]))
#print(find_record_multiple_values('test_2.csv',["first_name","last_name"]))
#remove_record_by_index('test_2.csv',["first_name","last_name"])
#get_remaining_values('test_2.csv', ["first_name","phone"])
#print(find_record_multiple_values('test_2.csv',["first_name","email"]))
#print(create_dictionary_file('test_2.csv',["first_name","phone","email"]))
#print(create_dictionary_input(["first_name","phone","email"]))
# print(find_record_value('test_2.csv', 'first_name', "Minna", 'remove'))
# count_records_value('test_2.csv', 'first_name', "Minna")
# count_records_key('test_2.csv',"phone")
# print(find_record_key('test_2.csv',"first_name"))
# option_list = ["first_name","email","phone"]
# generate_record(option_list)
# dictionary = get_all_records('test.csv')
# export_dictionary_to_file('test.csv', dictionary)
# remove_record('test.csv', 'first_name', "Minna")
# find_record('test.csv', 'first_name', "Minna")
# get_all_records('C:/Users/bpaczk/Desktop/python_training/10_10/100-contacts-kopia.csv')
#print(get_all_records('test_2.csv'))
# add_record('C:/Users/bpaczk/Desktop/python_training/10_10/100-contacts-kopia.csv', "bla, bla,bla")

#Abel,Maclead,Rangoni Of Florence,37275 St  Rt 17m M,Middle Island,Suffolk,NY,11953,631-335-3414,631-677-3675,amaclead@gmail.com

