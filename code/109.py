# computing the value of pi
# using the Leibnitz series:
# π/4 = 1 - 1/3 + 1/5 - 1/7 + ...

sign = 1
pi = 0
for i in range(1,10000000,2):
    pi += sign * 1/i
    sign *= -1

print(4 * pi) 

# Output:
# 3.1415924535897797
