# passing arbitrary number of
# arguments to a function

def my_f(*args):
    # notice the "*"
    print(f"Called with {len(args)} arg(s)")
    for index,value in enumerate(args):
        print(f"Arg #{index} = {value}")

my_f(5)
my_f(1,2)
my_f("a","b","c")

# Output:
# Called with 1 arg(s)
# Arg #0 = 5
# Called with 2 arg(s)
# Arg #0 = 1
# Arg #1 = 2
# Called with 3 arg(s)
# Arg #0 = a
# Arg #1 = b
# Arg #2 = c
