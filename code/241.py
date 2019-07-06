# comparing two files

import filecmp

file1 = "code/Data/file1.txt"
file2 = "code/Data/file2.txt"

print(filecmp.cmp(file1,file2))

# Output:
# True
