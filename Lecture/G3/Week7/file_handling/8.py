import os

filename = "2.txt"

# file = open(filename, "w")
# file.write("Last words before deletion...")
# file.close() # you need to close the file before deleting

with open(filename, "w") as file: 
    file.write("Last words before deletion...")

from time import sleep

sleep(3)

os.remove(filename)


