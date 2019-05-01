# parsing JSON from a file

import json

# 1. Open the file
with open("Data/test.json") as f:
    # 2. Parse JSON
    data = json.loads(f.read())

# what is the fourth letter?
print(data["letters"][3])

# Output:
# d
