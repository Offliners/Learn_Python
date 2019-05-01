# using the "zip" nuilt-in
# function

colours = ["red","green","yellow"]
fruits = ["apple","peer","banana"]

z = zip(colours,fruits)

for x in z:
    # x is a apple
    print(x[0] + " " + x[1])

# Output:
# red apple
# green peer
# yellow banana
