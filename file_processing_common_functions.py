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


def find_record_value(filename, key, value):
    all_records = get_all_records(filename)
    result = next((item for item in all_records if item[key] == value), False)
    if result != False:
        print("record exists")
    else:
        print("record does not exist")
    return result

def find_record_key(filename, key):
    all_records = get_all_records(filename)
    for record in all_records:

    result = next((item for item in all_records if item.get(key)), False)
    if result != False:
        print("record exists")
    else:
        print("record does not exist")
    return result

def remove_record(filename,key,value):
    all_records = get_all_records(filename)
    record_to_be_removed = find_record_value(filename, key, value)
    if record_to_be_removed != False:
        all_records.remove(record_to_be_removed)
    else:
        print("record does not exist")
    return all_records

def export_dictionary_to_file(filename,dict):
    #full_line = []
    with open(filename,'r+') as file:
            for record in dict:
                full_line = []
                for key in dict_keys:
                    current_line = record.get(key)
                    full_line.append(current_line)
                    line_to_write = ','.join(full_line)
                #print(line_to_write)
                add_record(filename, line_to_write)

def generate_record(option_list):
    output=[]
    record = dict.fromkeys(dict_keys, "Unknown")
    for element in option_list:
        value = common_functions.check_input("string",element)
        record[element] = value
    output.append(record)
    export_dictionary_to_file('test_2.csv', output)

def count_records_key(key):


def count_records_value(key,value):


#option_list = ["first_name","email","phone"]
#generate_record(option_list)
#dictionary = get_all_records('test.csv')
#export_dictionary_to_file('test.csv', dictionary)
#remove_record('test.csv', 'first_name', "Minna")
#find_record('test.csv', 'first_name', "Minna")
#get_all_records('C:/Users/bpaczk/Desktop/python_training/10_10/100-contacts-kopia.csv')
#add_record('C:/Users/bpaczk/Desktop/python_training/10_10/100-contacts-kopia.csv', "bla, bla,bla")