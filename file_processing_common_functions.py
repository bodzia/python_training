from copy import copy

import common_functions

dict_keys = ["first_name", "last_name", "company_name", "address", "city", "county", "state", "zip", "phone1", "phone", "email"]
#all_dict = []
#dict = {}

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


def find_record(filename, key, value):
    all_records = get_all_records(filename)
    result = next((item for item in all_records if item[key] == value), False)
    if result != False:
        print("record exists")
    else:
        print("record does not exist")

def remove_record(filename,key,value):
    all_records = get_all_records(filename)

#find_record('test.csv', 'first_name', "Minna")
#get_all_records('C:/Users/bpaczk/Desktop/python_training/10_10/100-contacts-kopia.csv')
#add_record('C:/Users/bpaczk/Desktop/python_training/10_10/100-contacts-kopia.csv', "bla, bla,bla")