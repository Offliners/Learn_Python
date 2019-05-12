# removing accents from characters

import unidecode

str = "Café München"

str = unidecode.unidecode(str)
print(str)

# Output:
# Cafe Munchen
