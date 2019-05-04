def filetextcount(fileinput):
    linescount = 0
    wordscount = 0
    charcount = 0

    # printing the contents of the file
    with open(fileinput,"r")as file:
        content = file.read()
        print("\nContent of file :\n" + content)
    
    with open(fileinput,"r") as file:
        for line in file:
            # splitting string and storing tje list in words variable
            words = line.split()
            linescount += 1 # incrementing lines count
            wordscount += len(words) # counting number of words
            # counting number of characters excluding space
            charcount += len(line) - line.count(" ")

    print("\nNumber of lines : %s" % str(linescount))
    print("Number of words : %s" % str(wordscount)) 
    print("Number of chars : %s" % str(charcount))

if __name__ == "__main__":
    fileinput = input("\nEnter file path : ")
    filetextcount(fileinput)
