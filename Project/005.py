def LeapYear(inputyear):
    # if a year is multiple of 4 and it shouldn't be multiple of 100.
    # every year cannot be multiple of 4. so if year is multiple
    # of 400 then the year is leap year.
    if inputyear % 4  == 0:
        if inputyear % 100 == 0:
            if inputyear % 400 == 0:
                print("\nThe %s is a leap year" % inputyear)
            else:
                print("\nThe %s is not a leap year" % inputyear)
        else:
            print("\nThe %s is a leap year" % inputyear)
    else:
        print("\nThe %s is not a leap year" % inputyear)

if __name__ == "__main__":
    year = int(input("\nEnter a year : "))
    LeapYear(year)
