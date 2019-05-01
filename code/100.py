# matching more than one number

import re

data = "2019-05-01"
match = re.search("(\d+)-(\d+)-(\d+)",data)

if match:
    print(match.groups())
    # this is a tuple:
    print(type(match.groups()))

# Output:
# ('2019', '05', '01')
# <class 'tuple'>
