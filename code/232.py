# catching "Ctrl + C"

c = 0 # counter
try:
    while 1: # infinite loop
        c += 1
except KeyboardInterrupt:
    print(f"The counter is {c} now") 

# Input:
# ^C

# Output:
# The counter is 142662630 now
