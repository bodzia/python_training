import os
path = r'/Users/bodzia/Desktop/python_training/'
for current_folder, subfolders, files in os.walk(path):
    print(f'current folder: {current_folder}')
    for subfolder in subfolders:
        print(f'{subfolder}')
        for file in files:
            print(f'{file}')