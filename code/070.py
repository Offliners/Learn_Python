# supplying defaults values
# for function arguments

def greet(name = "Dear"):
    print("Hello, " + name + "!")

greet("Eric")
greet()
greet("Karla")

# Output:
# Hello, Eric!
# Hello, Dear!
# Hello, Karla!
