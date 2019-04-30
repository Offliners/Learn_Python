# an example of using "format"
# with named arguments

first_name = "James"
last_name = "Bond"

greeting = \
    "My name is {last}. {first} {last}.".format(first = first_name,
                                                last = last_name)
print(greeting)

# Output:
# My name is Bond. James Bond.
