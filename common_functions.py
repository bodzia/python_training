def check_input (type, text):


    ask_for_input = True

    while ask_for_input:

        user_input = input(text)

        if type in ("string","float","int"):

            checked_value = check_value(type, user_input)

            if checked_value is True:
                ask_for_input = False
                if type == ("float"):
                    value = float(user_input)
                    return value
                elif type == ("int"):
                    value  = int(user_input)
                    return value
                else:
                    return user_input
            else:
                ask_for_input = True

        elif type == "list":
            try:
                elements_in_list = user_input.split(",")
            except:
                print("coś poszło nie tak...2")
                continue
            ask_for_input = False
            return elements_in_list

        else:
            print("coś poszło nie tak...3")
            ask_for_input = False
            break

def check_value(type, value):


    try:
        if type == "string":
            new_text = str(value).lower()
            return True
        elif type == "int":
            new_int = int(value)
            return True
        elif type == "float":
            new_float = float(value)
            return True

    except:
        print("coś poszło nie tak...")
        return False

def check_list(value, separator):
    try:
        new_value = value.split(separator)
    except:
        print("to nie lista")
    return new_value

def check_content(value, expected_value):
    for element in expected_value:
        if value == element:
            result = 'T'
            pass
            break
        else:
            result = 'F'
            continue
    if result == 'F':
        print("invalid value")
        quit(0)

def replace_string(value,character):
    for char in value:
        if char in character:
            value.replace(char, '')
    return value

def check_list_content(value_list, expected_value_list):
    i = 0
    number_of_elements = len(value_list)
    value_list = sorted(value_list)
    expected_value_list = sorted(expected_value_list)
    while i < number_of_elements:
        check_result = check_content(value_list[i], expected_value_list)
        i += 1
    return value_list
