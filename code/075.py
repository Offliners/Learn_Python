# what if you want a function
# that computes an area of
# both squares and rectangles?

def area(width,height = None):
    if height == None:
        height = width
    return height * width

print(area(20)) # square
print(area(20,30)) # rectangle

# Output:
# 400
# 600
