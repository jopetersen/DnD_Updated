import tkinter as tk
import random
import pickle

class Character:
    # initialize the empty character
    def __init__(self, name, race, strength, dexterity, wisdom, intelligence, constitution, charisma, weapons, items, spells):
        self.name = name
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.constitution = constitution
        self.charisma = charisma
        self.weapons = weapons
        self.items = items
        self.spells = spells

def character_creator():
    # Create a new character a-la-charactermancer
    print ("Test")

    # define a name
    name = input ("What is your character's name? ")

    #define which race a character is
    available_races = ("dwarf", "dragonborn", "elf", "gnome", "half-elf", "halfling", "half-orc", "human", "tiefling")
    race_value = input("Which race would you like to play as? " ).lower()

    #checking if a race is valid
    while (race_value not in available_races):
        print ("invalid race, please choose again!")
        race_value = input("Which race would you like to play as? " ).lower()
    print ("Your race is a " + race_value)


    stat_block = []
    num_stats = 6
     # rolling a 6 sided die 6 times to get the potential stat values
    while num_stats > 0:
        list_test = []
        for x in range(4):
            list_test.append(random.randint(1,6))
        list_test.remove(min(list_test))
        total = sum (list_test)
        stat_block.append(total)
        num_stats -= 1

    # expecting this to print out a list with 6 values
    # define a list of names for stats
    stat_names = ["strength", "dexterity", "wisdom", "charisma", "constitution", "intelligence"]

    stat_dictionary = {}
    print (stat_block)
    #stat assigning
    for index, name in enumerate(stat_names, start = 0):
        print ("Which value do you want to use for ", stat_names[index], "?")
        assigned_stat_value = int(input())
        if (assigned_stat_value in stat_block):
            print (stat_names)
            stat_dictionary.update({stat_names[index]:assigned_stat_value})
            print (stat_dictionary)
        else:
            print ("Not a valid number")
    #modify the stats based on race
    if (race_value == "dragonborn"):
        stat_dictionary["strength"] += 2
        stat_dictionary["charisma"] += 1
    elif (race_value == "dwarf"):
        stat_dictionary["constitution"] +=2
    elif (race_value == "elf"):
        stat_dictionary["dexterity"] += 2
    elif (race_value == "gnome"):
        stat_dictionary["intelligence"] += 2
    elif (race_value == "half-elf"):
        stat_dictionary["charisma"] += 2
        assigned_half_elf1 = input("Which 2 stats would you like to +1 to? ").lower()
        assigned_half_elf2 = input("Which other stat would you like to +1 to? ").lower()
        while (assigned_half_elf1 and assigned_half_elf2 not in stat_names):
            print ("Invalid Stats")
            assigned_half_elf1 = input("Which 2 stats would you like to +1 to? ").lower()
            assigned_half_elf2 = input("Which other stat would you like to +1 to? ").lower()
        stat_dictionary[assigned_half_elf1] += 1
        stat_dictionary[assigned_half_elf2] += 1
    elif (race_value == "halfling"):
        stat_dictionary["dexterity"] += 2
    elif (race_value == "half-orc"):
        stat_dictionary["strength"] += 2
        stat_dictionary["constitution"] += 1
    elif (race_value == "human"):
        stat_dictionary["dexterity"] += 1
        stat_dictionary["strength"] += 1
        stat_dictionary["intelligence"] += 1
        stat_dictionary["constitution"] += 1
        stat_dictionary["wisdom"] += 1
        stat_dictionary["charisma"] += 1
    elif (race_value == "tiefling"):
        stat_dictionary["intelligence"] += 1
        stat_dictionary["charisma"] += 2

    #print ("Making it here - race")
    weapons = []
    items = []
    spells = []

    char_1= Character(name, race_value, stat_dictionary["strength"], stat_dictionary["dexterity"], stat_dictionary["wisdom"], stat_dictionary["intelligence"], stat_dictionary["constitution"],stat_dictionary["charisma"], weapons, items, spells)

    print ("character created!")
    return char_1
    exit()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Create a Character",
                   command=character_creator)
slogan.pack(side=tk.LEFT)

root.mainloop()
