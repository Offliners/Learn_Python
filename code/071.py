# what happens when you return
# two values from a function

def f ():
    return 10,11

a,b = f()
print(a)
print(b)

# what if you only take one
c = f()
print(c)

# Output:
# 10
# 11
# (10, 11)
