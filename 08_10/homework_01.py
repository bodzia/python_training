#stworzyć funkcję która po otrzymaniu dwóch liczb
#będzie drukować niepełną piramidę. Dla liczba 5 i 7:
# #########
# ###########
# #############
import common_functions
#min_height = common_functions.check_input("int", "dolna granica: ")
#max_height = common_functions.check_input("int", "górna granica: ")

def build_pyramid(min_height, max_height):

    hash_number = min_height
    space_number = 0


    for x in range(min_height, max_height+1):
        max_hash_number = 2 * max_height - 2
        max_length = max_hash_number + 2
        space_number = int((max_length - hash_number) / 2)
        current_row_1 = " " * space_number
        current_row_2 = "#" * hash_number
        current_row_3 = " " * space_number
        current_row = current_row_1 + current_row_2 + current_row_3
        hash_number = hash_number + 2
        print(current_row)


build_pyramid(common_functions.check_input("int", "dolna granica: "),common_functions.check_input("int", "górna granica: "))
