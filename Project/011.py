import random

def BubbleSort(numlist):
    
    lenlist = len(numlist)

    # traverse through all elements in the list
    for i in range(lenlist):

        # last i elements are already in place
        for j in range(0,lenlist-i-1):

            # traverse through elements from 0 to lenlist - i - 1
            # if element is greater than next element
            # swap the element
            if numlist[j] > numlist[j + 1]:
                numlist[j] , numlist[j + 1] = numlist[j+1] , numlist[j]
    
    print("\nSorted list : ",end="")
    for i in range(lenlist):
        print(numlist[i],end=" ")

if __name__ == "__main__":

    # creating 10 random number upto the range of 100
    randomlist = random.sample(range(100),10)
    print("\nRandom list : ",end="")
    for k in range(len(randomlist)):
        print(randomlist[k],end=" ")

    # calling BubbleSort() function with
    # generated numbers
    BubbleSort(randomlist)
