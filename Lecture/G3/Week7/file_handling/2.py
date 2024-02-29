import os 

os.mkdir("dir1")

current_dir = os.getcwd()

print(current_dir)

os.mkdir(current_dir + "\dir2")