# test if all or any
# items are ture

data = [True,True,False]

if any(data):
    print("Some are True")
else:
    print("Not a single True")

if all(data):
    print("All are True")
else:
    print("Not all are True")

# Output:
# Some are True
# Not all are True
