# floating-point calculations
# are not always precise

a = 0.1 + 0.2 - 0.3
print(a)

from decimal import Decimal
b = Decimal("0.1") + \
    Decimal("0.2") - \
    Decimal("0.3")
print(b)

# Output:
# 5.551115123125783e-17
# 0.0
