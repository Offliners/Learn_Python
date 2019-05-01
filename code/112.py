# sweeping the content
# of two variables

left = "knift"
right = "fork"

print(f"Before: {left}, {right}")

left,right = right,left

print(f"After: {left}, {right}")

# Output:
# Before: knift, fork
# After: fork, knift
