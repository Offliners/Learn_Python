# using assert to break
# the program if your
# data are wrong

def divide(x,y):
    assert y != 0
    return x / y

a = divide(100,10) # OK
print(a)

a = divide(100,0) # Not OK
print(a) # will not be printed

# Output:
# 10.0
# Traceback (most recent call last):
#   File "c:/Users/ASUS/Desktop/Python/094.py", line 12, in <module>
#     a = divide(100,0) # Not OK
#   File "c:/Users/ASUS/Desktop/Python/094.py", line 6, in
# divide
#     assert y != 0
# AssertionError
