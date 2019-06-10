# removing an element from a list
# (if there more such elements)

# how to remove all "beta"s
data = ["alpha","beta","gamma","beta","delta"] # beta happens twice

data = [x for x in data if x != "beta"]
print(data)

# Output:
# ['alpha', 'gamma', 'delta']
