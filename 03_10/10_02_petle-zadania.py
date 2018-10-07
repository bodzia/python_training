# 2. Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
#
#   #
#  ###
# #####
 #######

import common_functions
height = common_functions.check_input("int", "wysokość: ")
hash_number = 1
space_number = 0
i = 0

while i < height:
    max_hash_number = 2 * height - 2
    max_length = max_hash_number + 2
    space_number = int((max_length - hash_number) / 2)
    current_row_1 = " " * space_number
    current_row_2 = "#" * hash_number
    current_row_3 = " " * space_number
    current_row = current_row_1 + current_row_2 + current_row_3
    print(current_row)
    hash_number = hash_number + 2

    i += 1

