# gauss the number

import random

while 1:
    n = random.randint(0,10)
    while 1:
        i = int(input("You gauss: "))
        if i > n:
            print("Too big")
        elif i < n:
            print("Too small")
        else:
            print("Correct!")
            break
    break

# Input:
# 5
# 7
# 9

# Output:
# You gauss: 5
# Too small
# You gauss: 7
# Too small
# You gauss: 9
# Correct!
