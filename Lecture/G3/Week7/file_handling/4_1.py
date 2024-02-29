file = open("1.py", "r") # "r" is the default mode

print(file.readline())

file.close()

file = open("1.py", "r")

print(file.readlines())

file.close()

file = open("1.py", "r")

print(file.read())

file.close()
