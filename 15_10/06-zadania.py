import os
import os.path

get_folder = os.getcwd()

files = os.listdir('..//')
#files = os.listdir(get_folder)
print(files)

for file in files:
    full_path = os.path.join(get_folder,file)
    print(full_path)