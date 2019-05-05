import math # importing python math package

# defining findPowerSet() set and size of the set
def findPowerSet(pset,setsize):
    # setting the size of the power set
    # of the set with setsize n is (2**n - 1)
    # empty set won't be printed
    powerSetSize = int(math.pow(2,setsize))
    print("\nPower set : ")

    # incrementing the counter values from 0
    # to the size of the power set
    for counter in range(0,powerSetSize):

        # increment the j values from 0
        # to size of the user entered set
        for j in range(0,setsize):

            # check if j-th bit in the counter is set
            # if set then print j-th element from set
            if (counter & (1 << j)) > 0:

                # printing the j-th element from the set
                print(pset[j],end="")
        print("") # printing the new line

if __name__ == "__main__":
    inputset = input("\nEnter elements of the set separated by commas : ")
    userset = inputset.split(",")
    size = len(userset)
    print("\nSet entered : " + str(userset))
    findPowerSet(userset,size)
