# generating a series
# of *different* random numbers

from random import randint

data = set() # set can contain each value only once

while len(data) < 20:
    r = randint(0,100)
    data.add(r) # new or existing number

print(len(data)) # got 20 items
print(data) # all different

# Output:
# 20
# {32, 34, 100, 6, 41, 74, 75, 12, 44, 14, 9, 80, 84, 21, 52, 55, 24, 57, 59, 28}
