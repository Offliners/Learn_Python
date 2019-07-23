# another way of incrementing
# all elements of a list

data = [10,20,30,40,50,60]

# let's use map and lambda
data = list(map(lambda x : x + 1,data))
print(data)

# Output:
# [11, 21, 31, 41, 51, 61]
