# take a string. remove all character
# that are not vowels. keep spaces
# for clarity

import re # regular expressions

s = "Hello, World! This is a string."

# sub = substitute

s2 = re.sub("[^aeiouAEIOU]+"," ",s) # vowels and a space replace with nothing

print(s2)

# Output:
# e o o i i a i
