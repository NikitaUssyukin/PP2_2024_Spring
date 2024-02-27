import os

path_to_file = './dir/subdir/30.txt'

file = open(path_to_file, "r")

print(file.read())

file.close()



