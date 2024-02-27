# checking access to the file

import os

path_to_file = input()

if os.path.exists(path_to_file):
    file = open(path_to_file)
    print(file.read())

