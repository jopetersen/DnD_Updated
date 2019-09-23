import random

# roll 4 dice
available_races = ("dwarf", "dragonborn", "elf", "gnome", "half-elf", "halfling", "half-orc", "human", "tiefling")

def race(race_list):
    race_value = input("Which race would you like to play as?" ).lower()
    while (race_value not in available_races):
        print ("invalid race, please choose again!")
        race_value = input("Which race would you like to play as?" ).lower()
    print ("Your race is a " + race_value)


stat_block = []
def stats(num_stats):
    while num_stats > 0:
        list_test = []
        for x in range(4):
            list_test.append(random.randint(1,6))
        list_test.remove(min(list_test))
        total = sum (list_test)
        stat_block.append(total)
        num_stats -= 1

# expecting this to print out a list with 6 values
# stats(6)


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



'''for index, name in enumerate(stat_names):
    stat_dictionary[name] = stat_block[index]
    print ("Which value do you want to use for ", stat_names[index], "?")
    assigned_stat_value = int(input())
    stat_dictionary[name] = stat_block[index]
'''
print (stat_dictionary)

# sets are like lists but can only have unique values
