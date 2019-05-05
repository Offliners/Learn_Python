import random

def SelectionSort(numlist):

    lenlist = len(numlist)

    for i in range(lenlist):

        # finding the minimum element in the
        # remaining list
        minimumElement = i
        for j in range(i + 1,lenlist):
            if numlist[minimumElement] > numlist[j]:
                minimumElement = j

        # swap the found minimum election with
        # first element
        temp = numlist[i]
        numlist[i] = numlist[minimumElement]
        numlist[minimumElement] = temp

    print("\nSorted list : ",end="")
    for i in range(lenlist):
        print(numlist[i],end=" ")

if __name__ == "__main__":
    #creating 10 random numbers upto the range of 100
    randomlist = random.sample(range(100),10)
    print("\nRandom list : ",end="")
    for k in range(len(randomlist)):
        print(randomlist[k],end=" ")

    # calling SelectionSort() function with
    # generated numbers
    SelectionSort(randomlist)
