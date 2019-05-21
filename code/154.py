# compile regular expressions to 
# make them faster

import re
from time import time

count = 0
t0 = time()

r = re.compile("\d") # compile it
for i in range(100000):
    if r.match(chr(i)):
        # use that compiled one
        count += 1

print(time() - t0)
print(count)

# Output:
# 0.06738734245300293
# 520
