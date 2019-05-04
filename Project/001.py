import random

def Game():
    randomNumber = random.randrange(0,5)
    tries = 0

    while True:
        print("\nTo End the Game Press 'E' ")
        inputNumber = input("Gauss a number between 0 to 5 : ")
        tries += 1

        if inputNumber.lower() == "e":
            print("\nThe number is " + str(randomNumber))
            break

        if int(inputNumber) < randomNumber:
            print("\nYour gauss was too small. Try again!")
        elif int(inputNumber) > randomNumber:
            print("\nYour gauss was too big. Try again!")
        else:
            print("\nYour gauss is correct")
            print("You gaussed " + str(randomNumber) + " in " + str(tries) + " tries")
            break

if __name__ == "__main__":
    Game()
