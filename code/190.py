data = ["alpha","beta","gamma","delta","beta","beta","epsilon"]

# find the positions of all "beta"s

# using list comprehension

pos = [x for (x,y) in enumerate(data) if y == "beta"]

print(pos) # positions of "beta"s

# Output:
# [1, 4, 5]
