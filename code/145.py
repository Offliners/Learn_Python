# nested "for" loops and "break"

for x in range(5):
    for y in range(5):
        if x == 3 or y == 3:
            break
        print(f"x = {x}, y = {y}")

# Output:
# x = 0, y = 0
# x = 0, y = 1
# x = 0, y = 2
# x = 1, y = 0
# x = 1, y = 1
# x = 1, y = 2
# x = 2, y = 0
# x = 2, y = 1
# x = 2, y = 2
# x = 4, y = 0
# x = 4, y = 1
# x = 4, y = 2
