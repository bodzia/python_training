
base = ["test, 1, 1", "test, 2, 2", "test, 3, 3"]
# copy = []
# for entry in base:
#     copy.append(entry + '\n')

copy = [entry + '\n' for entry in base]

with open ('base_test_file.csv', 'r+') as file:
    #file.writelines(copy)


    number_of_lines = sum(1 for line in open('base_test_file.csv'))
    i = 0
    while i < number_of_lines:
        current_line = file.readline()
        current_line = current_line.rstrip()
        new_line = current_line.split(",")
        new_line[1] = int(new_line[1])
        new_line[2] = float(new_line[2])
        base.append(new_line)
        #new_line = str(new_line)
        #file.write(new_line)
        i += 1


