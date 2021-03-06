# creating custom constructor
# and destructor for a  class

class C:
    def __init__(self):
        print("Constructor")
    def __del__(self):
        print("Destructor")

o = C() # constructor called
print("Hello, World!")

# destructor will be called
# at the end of the program

# Output:
# Constructor
# Hello, World!
# Destructor
