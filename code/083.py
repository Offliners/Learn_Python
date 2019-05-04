# reading from a text file

for str in open("code/Data/data.txt"):
    print(str, end="")

# we should not print the
# newline after each string,
# as "str" already contains it

# Output:
# line 1
# line 2
# line 3
