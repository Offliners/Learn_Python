# removing accents from characters
# need to pip install unidecode

import unidecode

str = "Café München"

str = unidecode.unidecode(str)
print(str)

# Output:
# Cafe Munchen
