from mylib import f

# using the function from mylib
print(f(5)) # 10

# define a local function
def f(x):
    # with different behaviour
    return 3 * x

# Same code as before
print(f(5)) # 15
# but different result

# Output:
# 10
# 15
