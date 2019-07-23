# getting prime numbers below 100
# using the sieve of Eratosthenes

n = 100
s = list(range(1,n+1))
p = 2
while p < n/2:
    for i in range(2 * p, n + 1, p):
        s[i - 1] = 0
    for i in range(0,n):
        if s[i] > p :
            p = s[i]
            break

s = list(filter(lambda x : x != 0,s))
print(s)

# Output:
# [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
