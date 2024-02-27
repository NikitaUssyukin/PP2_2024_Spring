# creating files in a directory

import os

directory = './dir/subdir/'

print(os.listdir(directory))

for i in range(1, 31):
    file = open(f"{directory}{i}.txt", "x") # in "x" mode if the file exists, you get an error
    file.close()