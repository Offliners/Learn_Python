# using more than one "for" in
# a list comprehension

nums = range(1,3)
table = [f"{x} + {y} = {x + y}"
         for x in nums # x = 1,2
         for y in nums # y = 1,2
        ]

print(table)
# for all combinations of 1 and 2

# Output:
# ['1 + 1 = 2', '1 + 2 = 3', '2 + 1 = 3', '2 + 2 = 4']
