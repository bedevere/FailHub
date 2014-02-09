#Copyright (c) Paul & John Ashby 2014
#Weight Effect
#This game is an RPG that is designed by my brother and myself (Paul).
#We built this to explore python programing, open source github, and to have some fun.
#

print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\\ \\ \\ \\ \\Weight Effect \\ \\ \\ \\ \\")
print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\nBy Paul & John Ashby")

main = input("\n\nWelcome, would you like to start a new game or exit?\n(new or exit)\n:>")

#------Imported Modules------#

import random

#------Defined Variables------#

wave = 1

#------Defined Lists------#

#dwarf: [name, str, dex, int, dam, arm, pot, hp, gold]
dwarf = [ 0, 0, 0, 0, 0, 0, 0, 0, 0]


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
        stat[0] = random.randint((2 * wave), (4 * wave)) #Determines the amount monsters in a wave.
        for i in range(1, 5):
                stat[i] = random.randint((5 * wave), (15 * wave)) #Generates the monsters stats.
        stat[5] = random.randint((3 * wave), (12 * wave)) #Generates monster
        stat[6] = random.randint((10 * wave * stat[0]), (25 * wave * stat[0])) #Generates the monsters health.
    
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
              "\n\tshop : Prints shop inventory.",
              "\n\tinv : Prints your inventory,",
              "\n\tbuy : Asks to buy an item from the shop.",
              "\n\texit : Exits the shop.")
              

def shop():
        store_inventory = []
        store_inventory.append(random.randint(1, 20) * wave) #Generates a random value weapon.
        store_inventory.append(random.randint(1, 18) * wave) #Generates a random value armor.
        store_inventory.append(random.randint(1, 6) * wave) #Generates a random number of potions.
        print("WELCOME TO YE OLD LOCAL SHOPPE")
        print("\nOur current inventory consists of the following items:")
        print("An axe that can do", store_inventory[0], "damage.")
        print("A set of armor that protects against", store_inventory[1], "points of damage.")
        print("We also have", store_inventory[2], "health potion(s).")
        shop_commands()
        sCommand = "nothing yet"
        while sCommand != "exit":
                sCommand = input("Please enter a command from the list.\n:> ")
                if sCommand == "list":
                        shop_commands()
                elif sCommand == "shop":
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
                                            dwarf[6] += numberPotions
                                            posEight -= (cost * numberPotions)
                                            dwarf[8] = posEight
                                        char_inventory()



def command():
        services = [1, 1, 0, 0] #Index 0 is a bedroll, 1 is the shop, 2 is the tome, and 3 is a beer seller
        time_left = 2
        
        print("\n\nThe camp is a low, cramped room off of the kobold tunnels.")
        
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
                        

def stance_set(oldstance): #takes an argument from previous function and names it 'oldstance'.
    #Looks at the argument list to see which stance the character is in and informs the player.
    if oldstance[0] == "Aggressive":
        print("\nYour current combat stance is 'Aggressive', you will",
        "\ndeal more damage but you will also take more as a result.")
    if oldstance[0] == "Balanced":
        print("\nYour current combat stance is 'Balanced', you will",
        "\nnot take any penalties.")
    if oldstance[0] == "Defensive":
        print("\nYour current combat stance is 'Defensive', you will",
        "\nbe better ready to defend yourself but may find it difficult",
        "\nto get a good attack in.")

    change = input("\nDo you want to change your stance?\n(y/n)\n:> ")
    
    if change == "y":
        print("\nHere are the stances available to you:",
        "\n(1) - Aggressive (increased attack, decreased armor)",
        "\n(2) - Balanced (no combat penalties)",
        "\n(3) - Defensive (increased armor, decreased attack)")
        
        newstance_number = int(input("Enter the number that corresponds to your choice and press enter.\n:> "))
        
        if newstance_number == 1:
            newstance = ["Aggressive"]
        elif newstance_number == 2:
            newstance = ["Balanced"]
        elif newstance_number == 3:
            newstance = ["Defensive"]
        print("\nYou have changed your combat stance to:", newstance[0])
        
        return newstance #returns the new stance
        
    else:
        return oldstance #returns the original stance
        
        
def initiative(monsters):
    monster_initiative = random.randint(1 + monsters[2], 20 + monsters[2])
    player_initiative = random.randint(1 + dwarf[2], 20 + dwarf[2])
    print("\nRolling initiative!")
    print("\nYou rolled a",player_initiative, "and the Kobolds rolled a", monster_initiative)
    if monster_initiative >= player_initiative:
        print("Looks like the Kobolds are attacking first, brace yourself.")
        turn = 2 #Sets round flag so monsters do damage first.
        return turn

    else:
        print("You attack first!")
        turn = 1 #Sets round flag so player does damage first.
        return turn

def player_attack(player_damage, number_monsters, total_monster_hp, monster_armor, stance):
    new_damage = round(player_damage + random.randint(1, 10))
    #test print
    #print("new_damage1 line 304 (expect 1 - 10 initially)", new_damage)
    #input()

    monster_deaths = 0
    
    new_damage += round(dwarf[4] - monster_armor) #Damage equals char damage - monster armor.
    #test print
    #print("new_damage2 line 309", new_damage)
    #input()
    
    if stance == "Aggressive": #Aggressive adds the character strength to the damage.
        stance_damage = dwarf[1]
    elif stance == "Balanced": #Balanced adds the character dexterity/4 to the damage.
        stance_damage = round(dwarf[2] / 4)
    elif stance == "Defensive": #Defensive adds the difference of the characters str and dex to the total damage.
        stance_damage = round(dwarf[1] - dwarf[2])
    #test print
    #print("stance_damage line 319", stance_damage)
    #input()
    
    new_damage += stance_damage #Adds/subtracts stance damage to new_damage.
    #test print
    #print("new_damage3 line 324", new_damage)
    #input()
    
    min_monster_hp = round(total_monster_hp / number_monsters) #Builds benchmark for min damage to kill monster.
    #test print
    #print("min_monster_hp line 329", min_monster_hp)
    #input()

    while new_damage >= min_monster_hp and number_monsters > 0:
        number_monsters -= 1
        monster_deaths += 1 #Used to subtract from total monsters.
        #Test print
        #print("Number of monsters left? ", number_monsters)
        #print("Number of monsters killed?", monster_deaths)
        input()
        new_damage -= min_monster_hp
        #Test print
        #print("new_damage remaining? (line 339)", new_damage)
        #input()
        total_monster_hp -= min_monster_hp
        #Test print
        #print("total_monster_hp remaining? (line 343) ", total_monster_hp)
        #input()
        
    if number_monsters <= 0 or new_damage < min_monster_hp:
        new_values = [new_damage, monster_deaths, total_monster_hp]
        return new_values


def monster_attack(monster_damage, player_armor, player_hp, stance):
    monster_damage += (random.randint(1 + wave, 10 + wave))
    if stance == "Defensive":
        monster_damage -= round(player_armor * 2)
    else:
        monster_damage -= player_armor
    if monster_damage <= 0:
        print("\nThe Kobolds attack doing", monster_damage, "damage!")
        print("You take no damage from the attack.")
        input("\nPress enter to continue.")
        return player_hp
    else:
        player_hp -= monster_damage
        print("\nThe Kobolds attack doing", monster_damage, "damage!")
        print("You have", player_hp, "health left.")
        input("Press enter to continue.")
        if player_hp <= 0:
            input("You have perished in combat!\n\nPress enter to continue.")
            exit()
        else:
            return player_hp
    

def combat(current_player_hp):
    #monsters: [num, str, dex, int, dam, arm, hp]
    monsters = ["0", "0", "0", "0", "0", "0", "0"]
    stat_modder(monsters, 1, 1, 4)
    #Test print
    #print("monsters (line 379)", monsters)
    
    print("\n\nPrepare yourself, you see", monsters[0], "Kobolds charging at you!")
    stance = ["Balanced"] #Sets the initial stance.
    player_damage_counter = 0 #Keeps track of how much damage the player does.
    new_loot = random.randint(50 * monsters[0] * wave, 100 * monsters[0] * wave)
    #Test print
    #print("new_loot (line 378)", new_loot)
    #input()
    
    while monsters[0] > 0 and dwarf[7] > 0:#loops until all monsters are dead or the player dies.
        stance = stance_set(stance) #Allows the player to change their stance before each round of combat.
        turn = initiative(monsters) #Rolls for initiative to see who goes first.
        check_move = 1 #Flag that notifies loop that player has or has not gone.
        if turn == 1:
            result = player_attack(player_damage_counter, monsters[0], monsters[6], monsters[5], stance[0])
            #test print
            #print("result list (line 401)", result)
            #input()
            
            player_damage_counter = result[0] #Updates total player damage.
            monsters[0] -= result[1] #Updates monsters left.
            monsters[6] = result[2] #Updates total monster HP.
            print("You have slain", result[1], "Kobolds this round! There are", monsters[0], "left.")
            if monsters[0] <= 0:
                print("You have slain all the Kobolds!")
                print("Congratulations!")
                dwarf[8] += new_loot
                print("You loot", new_loot, "gold from the slain kobolds.")
                input("\nPress enter to continue.")
                break
            turn = 2
            check_move = 0 #lets loop know player has already moved this round.
                
        if turn == 2:
            current_player_hp = monster_attack(monsters[4], dwarf[5], current_player_hp, stance)
            #test print
            #print("current_player_hp line 405:", current_player_hp)
            #input()
            
        if check_move == 1:
            result = player_attack(player_damage_counter, monsters[0], monsters[6], monsters[5], stance[0])
            #test print
            #print("checking result (second 'if') (line 427)", result)
            #input()
            
            player_damage_counter = result[0] #Updates total player damage.
            monsters[0] -= result[1] #Updates monsters left.
            monsters[6] = result[2] #Updates total monster HP.
            print("You have slain", result[1], "Kobolds this round! There are", monsters[0], "left.")
            if monsters[0] <= 0:
                print("You have slain all the Kobolds!")
                print("Congratulations!")
                dwarf[8] += new_loot
                print("You loot", new_loot, "gold from the slain kobolds.")
                input("\nPress enter to continue.")
                break
            
    return current_player_hp
                    

def loot(current_player_hp):
    print("\nYou have", current_player_hp, "health remaining.")
    print("You have", dwarf[6], "health potions remaining.")
    if dwarf[6] > 0:
        print("Do you want to use a health potion to restore your HP?\n(y,n)\n:>")
        use = input()
        if use == "y":
            dwarf[6] -= 1
            current_player_hp = dwarf[7]
            print("You have regained your health after drinking a potion.")
            print("You have", dwarf[7], "health and", dwarf[6], "potions remaining.")
            return current_player_hp
        else:
            print("Good luck then.")
            return current_player_hp
    else:
        input("Unfortunantely you don't have any potions to restore your health.\nPress enter to continue.")
        return current_player_hp
        
                
        
#------MAIN LOOP------#
while True:
        if main == 'new':
            for i in range(5): #This loop controls character creation.
                name = input("What is the name of your dwarf?\n:> ")
                stat_modder(dwarf, 0, name, 3)
                print("Generating stats for your dwarf!")
                stat_modder(dwarf, 1, 1, 1)
                char_inventory()
                reroll = input("Do you want to re-roll your character? (y/n)\n:> ")
                if reroll == "n":
                    break
                else:
                    print("You can re-roll your dwarf", 5 - (i + 1), "more times.")
            current_player_hp = dwarf[7]
        main = 'end'
        spend = input("Do you want to go to a shop before you fight endless waves of monsters?\n(y/n)\n:> ")
        if spend == "y":
            shop()
        print("Prepare for combat!")
        current_player_hp = combat(current_player_hp)
        loot(current_player_hp)
        wave += 1
        command()
