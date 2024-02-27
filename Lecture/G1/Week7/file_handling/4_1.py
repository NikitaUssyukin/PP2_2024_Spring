import os

file = open("ex2.txt", "w")

file.write("This data was written from 4_1.py using write() function!")

file.close()

file = open("ex2.txt", "r")

print(file.read())

file.close()



