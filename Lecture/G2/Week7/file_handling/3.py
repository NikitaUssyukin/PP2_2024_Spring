import os

print(os.path.exists('1.py')) # returns True if the file exists

filename = input()

print(os.path.exists(filename))