def ZellerCongruemce(month, day,year):
    # if January or February is entered 12 must be
    # added to the month and minus 1 from the year,
    # this puts in month 13 or 14 of previous year.

    if month == 1:
        month = 13
        year -= 1

    d = day         # day
    m = month       # month
    y = year        # year
    y1 = y % 100    # year of the century
    y2 = y // 100   # zero-based century

    # ZellerCongruemce = day + (13 * (month + 1) / 5) + y1 + (y1 / 4) + (y2 / 4) + y2 * 5
    zC = d + 13 * (m + 1) // 5 + y1 + y1 // 4 + y2 // 4 + y2 * 5

    # calculating remainder of d1 divide by 7
    d2 = zC % 7

    # use d2 value to find the day 
    if d2 == 2:
        return "Monday"
    elif d2 == 3:
        return "Thesday"
    elif d2 == 4:
        return "Wednesday"
    elif d2 == 5:
        return "Thursday"
    elif d2 == 6:
        return "Friday"
    elif d2 == 0:
        return "Saturday"
    elif d2 == 1:
        return "Sunday"

if __name__ == "__main__":
    print("\nMonth : \n1-Jan, 2-Feb, 3-Mar, 4-Apr, 5-May, 6-Jun,"
          "\n7-Jul, 8-Aug, 9-Sept, 10-Oct, 11-Nov, 12-Dec")
    dinput = input("\nEnter the date (D/MM/YYYY) : ").split("/") # splitting input the basic of "/"
    day = int(dinput[0])
    month = int(dinput[1])
    year = int(dinput[2])

    dMY = str(day) + "/" + str(month) + "/" + str(year)
    print("\n" + dMY + " is " + ZellerCongruemce(month,day,year)) 
