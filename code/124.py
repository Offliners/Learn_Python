# saving a data structure in a file

import pickle

data = {"alpha" : [3,5,7],
        "beta"  : [4,6,8]}

with open("code/Data/data.bin","wb") as f:
    pickle.dump(data,f)

# ...
with open("code/Data/data.bin","rb") as f:
    restored = pickle.load(f)
    print(restored)

# Output:
# {'alpha': [3, 5, 7], 'beta': [4, 6, 8]}
