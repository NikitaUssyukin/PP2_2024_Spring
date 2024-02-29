import os 

print(os.listdir())

path_to_folder = "../builtin_functions/" # relative path
absolute_path_to_folder = r"C:\Users\n.ussyukin\Documents\GitHub\PP2_2024_Spring\Lecture\G3\Week7\builtin_functions"
another_absolute_path = "C:\\Users\\n.ussyukin"

print(os.listdir(path_to_folder))
print(os.listdir(absolute_path_to_folder))
print(os.listdir(another_absolute_path))