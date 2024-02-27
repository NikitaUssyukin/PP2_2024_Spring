# file handling

# checking if the path is a directory or a file

import os

pathes = os.listdir()

for path in pathes:
    print("isfile():", os.path.isfile(path)) # checks if it is a file
    print("isdir():", os.path.isdir(path)) # checks if it is a directory