# printing the unicode names
# of the characters

import unicodedata

str = "Héļļö"

for s in str:
    print(unicodedata.name(s))

# Output:
# LATIN CAPITAL LETTER H
# LATIN SMALL LETTER E WITH ACUTE
# LATIN SMALL LETTER L WITH CEDILLA
# LATIN SMALL LETTER L WITH CEDILLA
# LATIN SMALL LETTER O WITH DIAERESIS
