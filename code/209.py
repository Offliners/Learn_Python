# using math.prod, a new function
# in the math module.
# available in Python 3.8+

import math

# factorial of 5
fact = math.prod(range(1,6))
# 1 * 2 * 3 * 4 * 5
print(fact)

# product of items
data = [3,4,7,8]
product = math.prod(data)
# = 3 * 4 * 7 * 8
print(product)

# Output:
# 120
# 672
