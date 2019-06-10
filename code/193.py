# polymorphism in python

class Animal:
    def talk(self):
        print("I am an animal")
class Dog(Animal):
    def talk(self):
        print("I am an dog")
class Cat(Animal):
    def talk(self):
        print("I am an cat")

# now make a list with objects of different
# classes from the above defined
zoo = [Dog(),Dog(),Cat(),Animal(),Cat()]

# and iterate over them:
for x in zoo:
    x.talk() # which "talk" method is called?

# Output:
# I am an dog
# I am an dog
# I am an cat
# I am an animal
# I am an cat
