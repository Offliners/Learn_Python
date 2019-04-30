# use "pass" to do nothing 
x = 0
while x < 8:
    x += 1
    if x == 4:
        pass
        # you need a block
        # here, so if you have
        # nothing to do,
        # type "pass"
    print(x)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
