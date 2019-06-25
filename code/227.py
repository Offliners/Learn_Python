# UUID v1 vs. UUID v4

import uuid

for _ in range(5):
    print(uuid.uuid1())

print("")

for _ in range(5):
    print(uuid.uuid4())

# Output:
# b330d4f8-975e-11e9-9a78-107b44b9d800
# b3320b46-975e-11e9-9299-107b44b9d800
# b3320b47-975e-11e9-b17f-107b44b9d800
# b3320b48-975e-11e9-b3ee-107b44b9d800
# b3320b49-975e-11e9-8af7-107b44b9d800

# 3ad4d2f7-7c37-4595-ae29-bf6d39e7f11a
# a5eb18d6-9d28-430d-a632-1249483d8a03
# e69f3265-8de3-4a7d-be84-6496febd7734
# 15455f9a-6e7e-4fd5-a004-723e2c361143
# 5dd2dede-294e-4201-a132-ff5732c97f8f
