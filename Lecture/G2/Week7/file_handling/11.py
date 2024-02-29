# deleting a folder

import os

os.rmdir("dir2") # you can only delete empty folders

print(os.path.exists("dir2"))