import random

def InsertionSort(numlist):

    lenlist = len(numlist)

    # traverse through 1 to len(arr)
    for i in range(1,lenlist):

        element = numlist[i]

        # move elements of lenlist, that are greater than
        # element, to one position ahead of current position
        j = i - 1
        while j >= 0 and element < numlist[j]:
            numlist[j + 1] = numlist[j]
            j -= 1
        numlist[j + 1] = element
    
    print("\n\nSorted list : ", end="")
    for i in range(lenlist):
        print(numlist[i],end=" ")

if __name__ == "__main__":
    # creating 10 random numbers upto the range of 100
    randomList = random.sample(range(100),10)
    print("\nRandom list : ",end="")
    for k in range(len(randomList)):
        print(randomList[k],end=" ")

    # calling InsertionSort() function with
    # generated numbers
    InsertionSort(randomList)
