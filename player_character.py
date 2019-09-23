import random

#creating a new player character
class player_character:

    # The constructor method is used to initialize data.
    #It is run as soon as an object of a class is instantiated.
    def __init__(self, name, stats, race):
        self.name = name
        self.stats = stats #this will be a dictionary
        self.race = race

# create a stat block for the characters
    def player_stats (self):
        stat_block = []
        def stats(num_stats):
            while num_stats > 0:
                list_test = []
                for x in range(4):
                    list_test.append(random.randint(1,6))
                #print(list_test)
                # remove the smallest value
                list_test.remove(min(list_test))
                #print ("New list value", list_test)
                #sum of items in a list
                total = sum (list_test)
                #testing the values of the list.
                #print("Sum of all elements in given list: ", total)
                stat_block.append(total)
                # adding to the greater array
                num_stats -= 1
        #expecting this to print out a list with 6 values
        stats(6)
        # define a list of names for stats
        stat_names = ["Strength", "Dexterity", "Wisdom", "Charisma", "Constitution", "Intelligence"]

        #initializing an empty dictionary

        stat_dictionary = {}
        #Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
        #This enumerate object can then be used directly in for loops or be converted into a list of tuples
        # using list() method.

        print (stat_block)

        for index, name in enumerate(stat_names, start = 0):
            print ("Which value do you want to use for ", stat_names[index], "?")
            assigned_stat_value = int(input())
            if (assigned_stat_value in stat_block):
                print (stat_names)
                stat_dictionary.update({stat_names[index]:assigned_stat_value})
                print (stat_dictionary)
            else:
                print ("Not a valid number")


        print (stat_dictionary)
    def name_of_character (self):
        name = input ("What is your character's name? ")
        # sets are like lists but can only have unique values
    def race (self):
        available_races = ("dwarf", "dragonborn", "elf", "gnome", "half-elf", "halfling", "half-orc", "human", "tiefling")
        race_value = input("Which race would you like to play as?" ).lower()
        while (race_value not in available_races):
            print ("invalid race, please choose again!")
            race_value = input("Which race would you like to play as?" ).lower()
        print ("Your race is a " + race_value)
