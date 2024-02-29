import os

path_to_folder = './dir/'

for i in range(1, 31):
    with open(path_to_folder + f"{i}.txt", "w") as file:
        file.write(f"This is {i}.txt, it was created and written from 11.py")