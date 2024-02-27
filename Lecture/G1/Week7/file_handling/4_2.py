import os

file = open("ex3.txt", "a")

file.write("This data was appended from 4_2.py using write() function!\n")

file.close()

file = open("ex3.txt", "r")

print(file.read())

file.close()



