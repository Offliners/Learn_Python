# what if you need to print
# two names?

name1,name2 = "John","Karla"

# old style
print("Hello, %s and %s!" %(name1,name2))

# new style
print("Hello, {} and {}!".format(name1,name2))

# Output:
# Hello, John and Karla!
# Hello, John and Karla!
