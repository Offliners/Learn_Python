# creating a class in Python
# using attributes to keep data

class Animal:
    def __init__(self,name): # Constructor
        self.name = name
    def talk(self):
        print("I am a " + self.name)

# creating an object or an instance

Animal1 = Animal("cat")
Animal1.talk()

# another object of the same class

Animal2 = Animal("dog")
Animal2.talk()

# Output:
# I am a cat
# I am a dog
