# convert a list of tuples
# to a list of lists

data = [(3,4),(7,8),(100,200)]

# using list comprehension
data2 = [list(a) for a in data] # "a" was a tuple here

print(data2)

# Output
# [[3, 4], [7, 8], [100, 200]]
