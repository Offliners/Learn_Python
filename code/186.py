# removing an element from a list
# (if there more such elements)

data = ["alpha","beta","gamma","beta","delta"] # beta happens twice

data.remove("beta")
print(data) # only the first "beta" is gone

data.remove("beta")
print(data) # now both are removed

# Output:
# ['alpha', 'gamma', 'beta', 'delta']
# ['alpha', 'gamma', 'delta']
