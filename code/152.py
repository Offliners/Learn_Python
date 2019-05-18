data = []

# you can add data of any type to
# a list in python

data.append(123) # number
data.append("Hi") # string
data.append(1 + 2j) # complex

class C:
    pass

o = C()
data.append(o) # object

for x in data:
    print(x)

# Output:
# 123
# Hi
# (1+2j)
# <__main__.C object at 0x000001E689BF9390>
