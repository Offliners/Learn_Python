import re

def EvenWords(fileinput):
    evenWords = 0
    with open(fileinput,"r") as file:
        content = file.read()
        print("\nContents of the file : \n",content)

    with open(fileinput,"r") as file:
        for line in file:
            words = re.split("[,.\s\n]*\s",line)
            for w in range(len(words)):
                if len(words[w]) % 2 == 0:
                    evenWords += 1
    print("\nNumber of even words : ",evenWords)

if __name__ == "__main__":
    filepath = input("Enter file path : ")
    EvenWords(filepath)
