# sorting a list of dictionaries by
# values

data = [{"name" : "Kevin","age" : 23},
        {"name" : "Mary","age" : 22}]

data.sort(key = lambda p : p["age"])
print(data)

# Output:
# [{'name': 'Mary', 'age': 22}, {'name': 'Kevin', 'age': 23}]
