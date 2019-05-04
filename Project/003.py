def textCount(line):
    linesCount = 0
    wordsCount = 0
    charCount = 0

    # splitting string and storing tje list in words variable
    words = line.split()
    linesCount += 1 # incrementing lines count
    wordsCount += len(words) # counting number of words
    # counting number of characters excluding space
    charCount += len(line) - line.count(" ")

    print("\nNumber of lines : %s" % str(linesCount))
    print("Number of words : %s" % str(wordsCount)) 
    print("Number of chars : %s" % str(charCount)) 

if __name__ == "__main__":
    lineinputs = input("\nEnter a line : ")
    textCount(lineinputs)
