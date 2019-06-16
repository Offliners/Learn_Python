# using the raw := operator
# in Python 3.8

# read and print lines before
# meet STOP

with open("Data/input.txt") as f:
    while(str := f.readline().strip() != "STOP":print(str))
