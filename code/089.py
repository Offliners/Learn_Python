# adding annotation to a function

def power(a : int,b : int) -> int:
    return a ** b

# function takes two "int"s and 
# return an "int"

print(power(2,3))

print(power.__annotations__)

# Output:
# 8
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
