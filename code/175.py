# remove newline characters from
# the strings in a list

data = ["alpha\n",
        "beta\n",
        "gamma\n"]

print(data)

def strip(s):
    return s.strip()

# let's use "map" this time
data = list(map(strip,data))
# map return an object of the "map" type
print(data)

# Output:
# ['alpha\n', 'beta\n', 'gamma\n']
# ['alpha', 'beta', 'gamma']
