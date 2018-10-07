def check_input (type, text):


    ask_for_input = True

    while ask_for_input:

        user_input = input(text)

        if type in ("string","float","int"):
            ask_for_input = check_value(type, user_input)
            continue

        if type == "list":
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

print(check_value("float", 0.4))