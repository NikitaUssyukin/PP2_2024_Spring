file = open("2.txt", "x") # opening a file in create mode

# by opening the file in 'x', 'w' or 'a' mode we create it

file.close() # closing the file

file = open("2.txt", "x") # in 'x' mode gives an error if the file already exists