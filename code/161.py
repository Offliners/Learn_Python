# caching function return values
# when you call it with the same
# argument(s)

from functools import lru_cache
# LRU = least recently used
@lru_cache(maxsize=1000)
def factorial(n):
    if n <= 1:
        return 1
    print(f"Computing {n}!")
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(3)) # uses cache

# Output:
# Computing 5!
# Computing 4!
# Computing 3!
# Computing 2!
# 120
# 6
