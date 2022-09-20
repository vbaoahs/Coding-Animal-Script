#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Animal:
#animal = input('Enter type of animal: ')
#name = input('Enter name: ')
#breed = input('Enter breed: ')

# Define the actions for each choice we want to offer.
    def dog_bark():
        print("\nbark\n")
    
    def cat_meow():
        print("\nmeow\n")
    
    def bird_chirp():
        print("\nchirp\n")
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def display_name(self):
        print(self.name)

# Give the user some context.
        print("\nWelcome to the animal center. What would you like to choose?")

# Set an initial value for choice other than the value for 'quit'.
    animal_type = ''

# Start a loop that runs until the user enters the value for 'quit'.
    while animal_type != 'q':
    # Give all the choices in a series of print statements.
        print("\n[1] Enter dog to choose dog.")
        print("[2] Enter cat  to choose cat.")
        print("[3] Enter bird  to choose bird.")
        print("[4] Enter list  to show what are applicable choices.")
        print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
        animal_type = input("\nWhat would you like to choose? ")
    
    # Respond to the user's choice.
        if animal_type == 'dog':
            dog_bark()
            name = input('Enter name: ')
            breed = input('Enter breed: ')
            fetch=input("Do you like fetch ? :")
            if fetch=="Yes" or fetch == "yes":
                print("Woof")
            else:
                print("Sad")
        elif animal_type == 'cat':
            cat_meow()
            name = input('Enter name: ')
            breed = input('Enter breed: ')
            angry=int(input("How Angry is your cat from 1-10?"))
            if angry == 1:
                print("Cool")
            elif angry == 10:
                print("Furious")
            else:
                print("Will be okay")
        elif animal_type == 'bird':
            bird_chirp()
            name = input('Enter name: ')
            breed = input('Enter breed: ')
            favorite_song=input("What is the bird's favorite song?")
        elif animal_type =='list':
            print("\n 1:Dog, 2: Cat, 3: Bird")
        elif animal_type == 'q':
            print("\nThanks for playing. See you later.\n")
        else:
            print("\nI don't understand that choice, please try again.\n")
            
class animal_type(Animal):
    pass

result = issubclass(animal_type, Animal)
print(result)

#Test
class Dog(Animal):
    dog1 = Dog("Max", "Boxer")
    dog1.display_name()
    print(dog1.breed)

class Cat(Animal):
    cat1 = Cat("Garfield", "Tabi")
    cat1.display_name()
    print(cat1.breed)

class Bird(Animal):
    bird1 = Bird("Lamar", "Raven")
    bird1.display_name()
    print(bird1.breed)
    
# Print a message that we are all finished.
print("Thanks again, bye now.")

