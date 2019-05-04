def FactorsOfNumber(number):
    print("\nThe factors of %s are :" % number)

    # finding the factors of the number
    for factors in range(1,number + 1):
        if number % factors == 0:
            print(factors)

if __name__ == "__main__":
    num = int(input("\nEnter a number : "))
    FactorsOfNumber(num)
