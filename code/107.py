# iterating over dictionary pairs
# (both keys and values)

capitals = {"France":"Paris",
            "Italy":"Rome"}

for country,city in capitals.items():
    # country = key
    # city = value
    print("The capatial of " + country + " is " + city + ".")

# Output:
# The capatial of France is Paris.
# The capatial of Italy is Rome.
