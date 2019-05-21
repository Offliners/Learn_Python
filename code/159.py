# the "id" function
class C:
    pass

# let's create two objects:
o1 = C()
o2 = C()

# and a variable pointing to one of them:
o3 = o2

# now let's see at their ids:
print(id(o1)) # an object
print(id(o2)) # a different object
print(id(o3)) # same object as o2

# Output:
# 1922764737056
# 1922764737280
# 1922764737280
