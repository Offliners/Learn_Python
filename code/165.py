# filtering ("grepping") data
# using comprehensions

data = list(range(10))
print(data)

# now filter it
# and select only small numbers

data = [x for x in data if x < 4]
print(data)

# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3]
