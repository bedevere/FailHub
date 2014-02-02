#Copywrite (c) Paul Ashby 2014
#Weight Effect
#First Game

print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\\ \\ \\ \\ Weight Effect \\ \\ \\ \\")
print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\nBy Paul Ashby")

main = input("\n\nWelcome, would you like to start a new game or exit?\n(new or exit)\n:>")

import random
def character_creation():
        print("Character Creation.")
        dwarf = []
        dwarf.append(input("Enter a name for your dwarf.\n:>"))
        print("Your dwarf is named", dwarf[0], ".")
        print("\nTime to roll your stats!")
        input("Press enter to roll for your strength.")
        dwarf.append(random.randint(1, 20)) #Str
        print("You rolled a", dwarf[1], "for your strength.")
        input("Press enter to roll for your dexterity.")
        dwarf.append(random.randint(1, 20)) #Dex
        print("You rolled a", dwarf[2], "for your dexterity.")
        input("Press enter to roll for your intelligence.")
        dwarf.append(random.randint(1, 20)) #Int
        print("You rolled a", dwarf[3], "for your inteligence.")
        input("Press enter to roll for your starting axe damage.")
        dwarf.append(random.randint(1, 20)) #Damage
        print("Your initial axe damage is", dwarf[4],".")
        input("Press enter to roll for your initial armor value.")
        dwarf.append(random.randint(1, 18)) #Armor
        print("Your inital armor will resist", dwarf[5], "points of damage.")
        dwarf.append(random.randint(0, 0)) #Potions
        print("You will start out with 0 potions.")
        input("Press enter to see your health (HP).")
        dwarf.append(100 + dwarf[1])
        print("Your initial HP is 100 plus your strength which comes to", dwarf[7], "HP.") 
        print("Here is what your character looks like so far."
              "\nName:", dwarf[0],
              "\nStrength:", dwarf[1],
              "\nDexterity:", dwarf[2],
              "\nInteligence:", dwarf[3],
              "\nDamage:", dwarf[4],
              "\nArmor:", dwarf[5],
              "\nPotions:", dwarf[6],
              "\nHP:", dwarf[7])

while main == "new":
    for i in range(5):
        character_creation()
        reroll = input("Do you want to reroll your character? (y/n)\n:>")
        if reroll == "n":
            break
        else:
            print("You can reroll your dwarf", 5 - (i + 1), "more times.")
    break
        
            
        
    
        
