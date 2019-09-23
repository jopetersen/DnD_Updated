ef race_stat_builder (race_list, num_stats):

    #defines which race you will be
    race_value = input("Which race would you like to play as?" ).lower()
    while (race_value not in available_races):
        print ("invalid race, please choose again!")
        race_value = input("Which race would you like to play as?" ).lower()
    print ("Your race is a " + race_value)

    stat_block = []

 #defines the base stat block
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
    stat_names = ["strength", "dexterity", "wisdom", "charisma", "constitution", "intelligence"]

    stat_dictionary = {}
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


    # sets are like lists but can only have unique values
