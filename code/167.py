# strings and "raw strings"

# a regular string
# with an escaped character
s1 = "a\tb"

# a raw string
# \t is not escaped and will
# appear as is
s2 = r"a\tb"

print(s1)
print(s2)

# Output:
# a       b
# a\tb
