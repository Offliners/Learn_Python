# print ASCII values of all
# characters in a given
# string

str = "Hello"

ascii = [ord(s) for s in str]

# ord() converts a character to
# its ASCII position number

print(ascii)

# Output:
# [72, 101, 108, 108, 111]
