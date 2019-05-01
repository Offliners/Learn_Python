# using iterators

my_list = ["alpha","beta","gamma"]

# make the list iterable
data = iter(my_list)

a = next(data)
print(a)

b = next(data)
print(b)

c = next(data)
print(c)

# Output:
# alpha
# beta
# gamma
