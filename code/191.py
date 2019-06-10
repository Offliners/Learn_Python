# how to get file size in bytes

import os

statinfo = os.stat("code/Data/data.txt")
print(statinfo.st_size)

# Output:
# 22
