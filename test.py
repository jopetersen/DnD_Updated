stat_names = ["Strength", "Dexterity", "Wisdom", "Charisma", "Constitution", "Intelligence"]

print (stat_names[0])

# prints "Strength"

while len(stat_names) > 0:
    x = 0
    #x will be used to iterate through the stat_names list
    print ("Here is your list of possible stat values: ", stat_block)
    print ("Which stat value do you want to assign to ", stat_names[x], "?")
    assign = input()
    # checks to see if the number entered is in the stat_values, if it is then it will add it to thedictionary & remove that stat
    if (assign in stat_block):
        print ("Great! ", assign, " is now your ", stat_block)
        stat_dictionary.update({stat_names[x]:assign})
        stat_names.remove(stat_names[x])
        stat_block.remove(assign)
        x+=1
    else:
        print ("invalid number")




    for i in range (0, len(stat_names)):
        x = 0
        #x will be used to iterate through the stat_names list
        print ("Here is your list of possible stat values: ", stat_block)
        print ("Which stat value do you want to assign to ", stat_names[x], "?")
        assign = input()
        x+=1
        # checks to see if the number entered is in the stat_values, if it is then it will add it to thedictionary & remove that stat
        if (assign in stat_block):
            print ("Great! ", assign, " is now your ", stat_block)
            stat_dictionary.update({stat_names[x]:assign})
            stat_names.remove(stat_names[x])
            stat_block.remove(assign)
        else:
            print ("invalid number")


iterable_range = len(stat_names)
i = 0
print ("Here is your list of possible stat values: ", stat_block)
while iterable_range > 0:
    print ("Which stat value do you want to assign to ", next(stat_names_iter), "?")
    assign = input()
    i+= i
    if (assign in stat_block):
        print ("Great! ", assign, " is now your ", stat_block)
        stat_dictionary.update({stat_names[x]:assign})
        stat_names.remove(stat_names[x])
        stat_block.remove(assign)
    else:
        print ("invalid number")






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
        def name (self):
            name = input ("What is your character's name? ")
            # sets are like lists but can only have unique values
