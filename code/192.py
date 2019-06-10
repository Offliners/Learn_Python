# how to check if the file
# or directory exists

import os

print(os.path.exists("code/Data/data.txt"))
print(os.path.exists("code/Data/none.txt"))

# also with directories
print(os.path.exists("code/__pycache__"))

# Output:
# True
# False
# True
