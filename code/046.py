# using "break"
# to stop the loop

x = 0
while x < 1000:
    print(x)
    x += 1
    if x == 5:
        break

print("done")

# Output:
# 0
# 1
# 2
# 3
# 4
# done
