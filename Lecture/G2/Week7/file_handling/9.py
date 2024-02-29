# creating 30 files with sequenced names

import os

path_to_file = './dir/subdir/'

os.mkdir(path_to_file)

for i in range(1, 31):
    file = open(f"{path_to_file}{i}.txt", "w")
    file.write(f"You're in {file.name}, this was written from 9.py")
    file.close()