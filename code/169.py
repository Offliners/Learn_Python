# frozen sets

data = [10,20,30]

# create a frozen set
my_set = frozenset(data)
# my_set.add(40) # error

print(my_set)

# Output:
# frozenset({10, 20, 30})
