def check_input (type, text):


    ask_for_input = True

    while ask_for_input:

        user_input = input(text)

        if type == "string":
            try:
                new_text = str(user_input).lower()
            except:
                print("coś poszło nie tak...1")
                continue

            ask_for_input = False
            return new_text

        if type == "int":
            try:
                new_int = int(user_input)

            except:
                print("próbuj dalej...")
                continue

            ask_for_input = False
            return new_int

        if type == "float":
            try:
                new_float = int(user_input)

            except:
                print("próbuj dalej...")
                continue

            ask_for_input = False
            return new_float

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

    if type == "string":
        try:
            new_text = str(value).lower()
            return new_text
        except:
            print("coś poszło nie tak...1")



    if type == "int":
        try:
            new_int = int(value)
            return new_int

        except:
            print("próbuj dalej...")



    if type == "float":
        try:
            new_float = float(value)
            return new_float

        except:
            print("próbuj dalej...")
            exit(1)



    else:
        print("coś poszło nie tak...3")

