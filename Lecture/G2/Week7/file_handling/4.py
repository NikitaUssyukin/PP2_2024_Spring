import os

path_to_dir = r'C:\Users\n.ussyukin\Desktop\PP2\PP2_2024_Spring\Lecture\G2\Week7\file_handling'

# or
# path_to_dir = os.getcwd()

dirs = os.listdir(path_to_dir)

for dir in dirs:
    print(dir)
    print("isdir:", os.path.isdir(dir))
    print("isfile:", os.path.isfile(dir))
    print("# -----")