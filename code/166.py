# filtering data using a 
# built-in function "filter"

data = list(range(10))
print(data) # 10 numbers

def my_filter(x):
    # your custom filtering function
    return x < 4
    # only selects small numbers

data = list(filter(my_filter,data))
print(data) # four items left

# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3]
