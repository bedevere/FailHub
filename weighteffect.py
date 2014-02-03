#Copywrite (c) Paul & John Ashby 2014
#Weight Effect
#First Game

print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\\ \\ \\ \\ Weight Effect \\ \\ \\ \\")
print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\nBy Paul & John Ashby")

main = input("\n\nWelcome, would you like to start a new game or exit?\n(new or exit)\n:>")

#------Imported Modules------#
import random
#------Defined Variables------#
wave = 1
#------Defined Lists------#
dwarf = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

#------Defined Functions------#
def char_inventory():
        print("Here is what your character looks like so far."
              "\nName:", dwarf[0],
              "\nStrength:", dwarf[1],
              "\nDexterity:", dwarf[2],
              "\nIntelligence:", dwarf[3],
              "\nDamage:", dwarf[4],
              "\nArmor:", dwarf[5],
              "\nPotions:", dwarf[6],
              "\nHP:", dwarf[7],
              "\nGold:", dwarf[8])

def stat_modder(x, y, z, a):
#x is the stat list, y is the stat location,
#z is the new value, a is the command flag
    stat = x

    if (a == 1):#A 1 value for A mean generate character stats
        for i in range(1, 5):
            stat[i] = random.randint(5,20)
        stat[5] = random.randint(3, 18)
        stat[7] = 100 + stat[1]
        stat[8] = random.randint(50, 100)

    elif(a == 2):#A 2 value for A means generate magic stats
        for i in range(3):
            stat[i] = random.randint(1, 20)
        stat[3] = 1
        stat[4] = 1

    elif(a == 3):#A 3 value for A means modify a stat
        stat[y] = z
    
    elif(a == 4): #A 4 value for A means generate stats for a monster wave.
        stat[0] = random.randint((2 * wave), (4 * wave))
        for i in range(1, 5):
                stat[i] = random.randint((5 + wave), (15 + wave))
        stat[5] = random.randint((3 + wave), (12 + wave))
        stat[6] = random.randint((10 * wave * stat[0]), (25 * wave * stat[0]))
    
    else:
        print('Burn the heretic')
    return stat

def shop_commands():
        print("List of commands:",
              "\nlist : Shows list of commands.",
              "\nshopinv : Prints shop inventory.",
              "\ninv : Prints your inventory,",
              "\nbuy : Asks to buy an item from the shop.",
              "\nexit : Exits the shop.")

def shop():
        store_inventory = []
        store_inventory.append(random.randint(1, 20) * wave) #Weapons
        store_inventory.append(random.randint(1, 18) * wave) #Armor
        store_inventory.append(random.randint(1, 6) * wave) #Potions
        print("WELCOME TO YE OLD LOCAL SHOPPE")
        print("Our current inventory consists of the following items:")
        print("An axe that can do", store_inventory[0], "damage.")
        print("A set of armor that protects against", store_inventory[1], "points of damage.")
        print("We also have", store_inventory[2], "health potion(s).")
        shop_commands()
        sCommand = "nothing yet"
        while sCommand != "exit":
                sCommand = input("Please enter a command from the list.\n:> ")
                if sCommand == "list":
                        shop_commands()
                elif sCommand == "shopinv":
                        print("Our current inventory consists of the following items:")
                        print("An axe that can do", store_inventory[0], "damage.")
                        print("A set of armor that protects against", store_inventory[1], "points of damage.")
                        print("We also have", store_inventory[2], "health potion(s).")
                elif sCommand == "inv":
                        print("You have the following in your inventory.",
                              "\nAn axe that can do", dwarf[4], "damage.",
                              "\nA set of armor that can withstand", dwarf[5], "points of damage.\n",
                              dwarf[6], "Health potions.\n",
                              dwarf[8], "Gold.")
                elif sCommand == "buy":
                        print("You can buy the following items:")
                        print("(1) = Axe",
                              "\n(2) = Armor",
                              "\n(3) = Potions")
                        purchase = input("Buy an item from the shop by entering the number that coorosponds to that item.\n:> ")
                        if purchase == "1": #buying the axe.
                                cost = store_inventory[0] * 3 * wave
                                print("This axe will cost", cost, "gold.")
                                purchase = input("Do you still want to buy this axe?\n(y/n)\n:> ")
                                if purchase == "y":
                                        posEight = int(dwarf[8])
                                        if posEight < cost:
                                                print("YOU DON'T HAVE THAT KIND OF MONEY!")
                                                break
                                        else:
                                            del dwarf[4]
                                            dwarf.insert(4, store_inventory[0])
                                            posEight -= cost
                                            del dwarf[8]
                                            dwarf.insert(8, posEight)
                                        char_inventory()
                                else:
                                    break
                        elif purchase == "2": #buying the armor.
                                cost = store_inventory[1] * 3 * wave
                                print("This armor will cost", cost, "gold.")
                                purchase = input("Do you still want to buy this armor?\n(y/n)\n:> ")
                                if purchase == "y":
                                        posEight = int(dwarf[8])
                                        if posEight < cost:
                                                print("YOU DON'T HAVE THAT KIND OF MONEY!")
                                                break
                                        else:
                                            del dwarf[5]
                                            dwarf.insert(5, store_inventory[1])
                                            posEight -= cost
                                            del dwarf[8]
                                            dwarf.insert(8, posEight)
                                        char_inventory()
                                else:
                                    break
                        elif purchase == "3": #buying some potions.
                                cost = 25 * wave
                                print("Each potion will cost", cost, "gold.")
                                purchase = input("Do you still want to buy some potions?\n(y/n)\n:> ")
                                if purchase == "y":
                                        numberPotions = int(input("How many potions do you want to buy?\n:> "))
                                        if numberPotions > store_inventory[2]:
                                                print("THERE ARE NOT THAT MANY POTIONS IN THE STORE!")
                                                break
                                        posEight = int(dwarf[8])
                                        if posEight < (cost * numberPotions):
                                                print("YOU DON'T HAVE THAT KIND OF MONEY!")
                                                break
                                        else:
                                            del dwarf[6]
                                            dwarf.insert(6, numberPotions)
                                            posEight -= (cost * numberPotions)
                                            del dwarf[8]
                                            dwarf.insert(8, posEight)
                                        char_inventory()
                                else:
                                    break


def wave_combat():
        monster_wave = ["0", "0", "0", "0", "0", "0", "0"]
        stat_modder(monster_wave, 1, 1, 4)
        print("Prepare yourself, you see", monster_wave[0], "Kobolds charging at you!")
        while monster[0] > 0 and dwarf[7] > 0:#loops until all monsters are dead or the player dies.
                
        
        
#------MAIN LOOP------#
while main == 'new':
    for i in range(5): #This loop controls character creation.
        name = input("What is the name of your dwarf?\n:> ")
        stat_modder(dwarf, 0, name, 3)
        print("Generating stats for your dwarf!")
        stat_modder(dwarf, 1, 1, 1)
        char_inventory()
        reroll = input("Do you want to reroll your character? (y/n)\n:> ")
        if reroll == "n":
            break
        else:
            print("You can reroll your dwarf", 5 - (i + 1), "more times.")
            
    spend = input("Do you want to go to a shop before you fight endless waves of monsters?\n(y/n)\n:> ")
    if spend == "y":
            shop()
    print("Prepare for combat!")
    wave_combat()
    
    break
