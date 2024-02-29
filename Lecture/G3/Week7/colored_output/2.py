from colorama import Fore, Back, Style

import os 

path = "C:\\Users\\n.ussyukin"

dir_list = os.listdir(path)

with os.scandir(path) as it:
    for entry in it:
        if entry.is_file():
            print(Fore.CYAN + entry.name)   
        else:
            print(Fore.GREEN + entry.name)

# with os.scandir(path) as it:
#     for entry in it:
#         if entry.is_dir():
#             print(Fore.GREEN + entry.name)

print(Style.RESET_ALL)