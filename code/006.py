# deleting a variable

x = 42
print(x)

# now delete it
del(x)
print(x) # will not be able to print 

# Output:
# Traceback (most recent call last):
#   File "006.py", line 8, in <module>
#     print(x) # will not be able to print
# NameError: name 'x' is not defined
