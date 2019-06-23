# compute the area of a triangle
# (having its three sides)
# let's transform the code

import math

a = []
for i in range(3):
    a.append(float(input(f"Side {i+1} : ")))

s = sum(a) / 2
area = math.sqrt(s * math.prod(map(lambda x : s - x,a)))
# math.prod : available in python 3.8+
print(f"The area is {area}")

# Input:
# 3
# 4
# 5

# Output:
# The area is 6.0
