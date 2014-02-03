#Copywrite (c) Paul & John Ashby 2014
#Weight Effect
#This game is an RPG that is designed by my brother and myself (Paul).
#We built this to explore python programing, open source github, and to have some fun.
#

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

#dwarf: [name, str, dex, int, dam, arm, pot, hp, gold]
dwarf = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]

#------Defined Functions------#
def char_inventory():#Prints out the stats of the player.
        print("Here is what your character looks like so far."
              "\n\nName:", dwarf[0],
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

def magic(command):
    #Stats are as follows, 0=Self Knowledge, 1=Will, 2=Concentration 3=Lore
    #4=Corruption
    dwarf_magic = [0, 0, 0, 0, 0]

    if(command == 'read dark tome'):#Boom, long slippery slope baby...
        print("""As you brush the dust from the cover of the dark tome,
a chill runs up your arm. A glance down reveals the title,
'Meditations on the Unseen Worlds'. You slowly open the 
book and begin to read...""")

        print("""It seems to be a journal written by a scholar detailing his
exploration of these supposed unseen worlds. He goes into great
detail in his methods and you think you could replicate his
work. """)

        path = input("""Do you stop reading?
(yes or no):> """)        

        if(path == 'yes'):
            print("Scoffing at the madman's claims, you toss the book to the side.")
            
        else:
            print("Drawn on by his compelling claims, you continue to read the book...")

            dwarf_magic = stat_modder(dwarf_magic, 0, 0, 2)
            print("Following the tome's direction, you determine your mental status...")
            stat = (dwarf_magic[1] + (20-dwarf_magic[0]))
            if(stat < 15):
                print("You think your Will is poor.")
            elif(15 < stat < 30):
                print("You think your Will is average.")
            else:
                print("You think your Will is great!")

            stat = (dwarf_magic[2] + (20-dwarf_magic[0]))
            if(stat < 15):
                print("You think your Concentration is poor.")
            elif(15 < stat < 30):
                print("You think your Concentration is average.")
            else:
                print("You think your Concentration is great!") 


def shop_commands():#Lists all the commands for the shopping loop.
        print("\nList of commands:",
              "\n\tlist : Shows list of commands.",
              "\n\tshopinv : Prints shop inventory.",
              "\n\tinv : Prints your inventory,",
              "\n\tbuy : Asks to buy an item from the shop.",
              "\n\texit : Exits the shop.")

def shop():
        store_inventory = []
        store_inventory.append(random.randint(1, 20) * wave) #Generates a random value weapon.
        store_inventory.append(random.randint(1, 18) * wave) #Generates a random value armor.
        store_inventory.append(random.randint(1, 6) * wave) #Generates a random number of potions.
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
                              "\n\nAn axe that can do", dwarf[4], "damage.",
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
                                                input("No purchase made, press enter to continue.")
                                        else:
                                            del dwarf[4]
                                            dwarf.insert(4, store_inventory[0])
                                            posEight -= cost
                                            del dwarf[8]
                                            dwarf.insert(8, posEight)
                                        char_inventory()

                        elif purchase == "2": #buying the armor.
                                cost = store_inventory[1] * 3 * wave
                                print("This armor will cost", cost, "gold.")
                                purchase = input("Do you still want to buy this armor?\n(y/n)\n:> ")
                                if purchase == "y":
                                        posEight = int(dwarf[8])
                                        if posEight < cost:
                                                print("YOU DON'T HAVE THAT KIND OF MONEY!")
                                                input("No purchase made, press enter to continue.")
                                        else:
                                            del dwarf[5]
                                            dwarf.insert(5, store_inventory[1])
                                            posEight -= cost
                                            del dwarf[8]
                                            dwarf.insert(8, posEight)
                                        char_inventory()
                                        
                        elif purchase == "3": #buying some potions.
                                cost = 25 * wave
                                print("Each potion will cost", cost, "gold.")
                                purchase = input("Do you still want to buy some potions?\n(y/n)\n:> ")
                                if purchase == "y":
                                        numberPotions = int(input("How many potions do you want to buy?\n:> "))
                                        if numberPotions > store_inventory[2]:
                                                print("THERE ARE NOT THAT MANY POTIONS IN THE STORE!")
                                                input("Press enter to go back to the shop menu.")
                                        posEight = int(dwarf[8])
                                        if posEight < (cost * numberPotions):
                                                print("YOU DON'T HAVE THAT KIND OF MONEY!")
                                                input("No purchase made, press enter to continue.")
                                        else:
                                            del dwarf[6]
                                            dwarf.insert(6, numberPotions)
                                            posEight -= (cost * numberPotions)
                                            del dwarf[8]
                                            dwarf.insert(8, posEight)
                                        char_inventory()



def command():
        services = [1, 1, 0, 0] #Index 0 is a bedroll, 1 is the shop, 2 is the tome, and 3 is a beer seller
        time_left = 2
        
        print("The camp is a low, cramped room off of the kobold tunnels.") 
        
        if(services[0] == 1):
                print("You see a drab straw bedroll shoved in the corner.")
        if(services[1] == 1):
                print("You see a battered looking tinker standing near a cart of wares.")
        if(services[2] == 1):
                print("You see a dark tome lying on a table.")
        if(services[3] == 1):
                print("You see a beerseller partying by the fire.")
        while(time_left > 0):
                user_command = input("What would you like to do? (shop, read, sleep, party):> ")
        
                if (user_command == 'shop' and services[1] == 1):
                        shop()
                        time_left -= 1
                elif (user_command == 'sleep' and services[0] == 1):
                        print("Weary, you collapse onto the bedroll try to sleep")
                        time_left -= 1
                elif (user_command == 'read' and services[2] == 1):
                        magic(read)
                        time_left -= 1
                elif (user_command == 'party' and services[3] == 1):
                        print("Are you insane?")
                        time_left -= 1
                else:
                        print("What?")

def wave_combat():
        monster_wave = ["0", "0", "0", "0", "0", "0", "0"]
        stat_modder(monster_wave, 1, 1, 4)
        print("Prepare yourself, you see", monster_wave[0], "Kobolds charging at you!")
        #while monster_wave[0] > 0 and dwarf[7] > 0:#loops until all monsters are dead or the player dies.
            #Do stuff!        
        
        
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
