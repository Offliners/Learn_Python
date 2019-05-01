# demonstrating list comprehensions

def f(x):
    return x ** 2

# create a list of squares
data = [f(x) for x in range(10)]

# print the content of "data"
for x in range(10):
    print(f"{x}² = {data[x]}")

# Output:
# 0² = 0
# 1² = 1
# 2² = 4
# 3² = 9
# 4² = 16
# 5² = 25
# 6² = 36
# 7² = 49
# 8² = 64
# 9² = 81
