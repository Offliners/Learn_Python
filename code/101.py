# case-insensitive matching
# with regular expressions

import re
str = ["Word","word","wORD","Hi"]
for s in str:
    print("Testing " + s + "...",end="")
    if re.match("word",s,re.IGNORECASE): # add this flag
        print("OK")
    else :
        print("Not OK")

# Output:
# Testing Word...OK
# Testing word...OK
# Testing wORD...OK
# Testing Hi...Not OK
