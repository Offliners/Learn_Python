# multiplying by 2 using shift

val = 10
val <<= 2 # mul by 4
print(val)

val = 1
for _ in range(5):
    val <<= 1 # *= 2
    print(val)

# Output:
# 40
# 2
# 4
# 8
# 16
# 32
