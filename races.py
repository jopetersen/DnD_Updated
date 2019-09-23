available_races = ("dwarf", "dragonborn", "elf", "gnome", "half-elf", "halfling", "half-orc", "human", "tiefling")

race_value = input("Which race would you like to play as?" ).lower()

while (race_value not in available_races):
    print ("invalid race, please choose again!")
    race_value = input("Which race would you like to play as?" ).lower()

print ("Your race is a " + race_value)
