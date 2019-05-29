# remove newline characters from
# the strings in a list

data = ["alpha\n",
        "beta\n",
        "gamma\n"]

print(data)

data = list(map(lambda s : s.strip(),data))
# map return an object of the "map" type
print(data)

# Output:
# ['alpha\n', 'beta\n', 'gamma\n']
# ['alpha', 'beta', 'gamma']
