# getting line number N from
# a text file

import linecache

line_n = linecache.getline("code/Data/greek.txt",4)

print(line_n)

# Output:
# delta
