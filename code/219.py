# count letters in the given text
# print the states in descending order

message = "Hello, World!"
stats = {letter:message.count(letter) for letter in message} # dictionary comprehension

for x in sorted(stats,key=stats.get,reverse=True):
    # sort by value, descending order
    print(f"{x} = {stats[x]}")

# Output:
# l = 3
# o = 2
# H = 1
# e = 1
# , = 1
#   = 1
# W = 1
# r = 1
# d = 1
# ! = 1
