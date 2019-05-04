import cmath

def QuadraticEquation(a,b,c):

    # calculating the discreminant
    d = (b ** 2) - (4 *a * c)

    # finding the solutions
    numerator1 = -b + cmath.sqrt(d)
    denominator1 = 2 * a
    solution1 = numerator1 / denominator1

    numerator2 = -b - cmath.sqrt(d)
    denominator2 = 2 * a
    solution2 = numerator2 / denominator2

    print("The solutions are %s and %s" % (solution1,solution2))

if __name__ == "__main__":
    print("\nEnter the values of a , b and c in ax² + bx + c = 0")
    a = float(input("Enter a : "))
    b = float(input("Enter b : "))
    c = float(input("Enter c : "))
    QuadraticEquation(a,b,c)
