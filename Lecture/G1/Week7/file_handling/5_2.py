# creating files in a directory

import os

directory = './dir/subdir/'

print(os.listdir(directory))

for i in range(1, 31):
    file = open(f"{directory}{i}.txt", "w") # in "w" mode if the file exists, you don't get an error
    file.close()