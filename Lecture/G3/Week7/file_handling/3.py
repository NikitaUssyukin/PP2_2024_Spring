import os 

dirs_list = os.listdir()

for dir in dirs_list:
    print(dir)
    print(os.path.isfile(dir))
    print(os.path.isdir(dir))
    print("-----")