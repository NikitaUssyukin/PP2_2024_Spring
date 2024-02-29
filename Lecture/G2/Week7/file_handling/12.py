# checking access to file

import os

filename = input()

print(os.access(filename, os.F_OK)) # existence
print(os.access(filename, os.R_OK)) # readability
print(os.access(filename, os.W_OK)) # writability
print(os.access(filename, os.X_OK)) # executability