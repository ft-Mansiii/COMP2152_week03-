import random

# Dice Options USing List
diceOptions = list(range(1, 7))

# Weapons Array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']
print("Available Weapons:", ', '.join(weapons))

#Inputs combat strength hero
combatStrength = int(input("Enter your combat strength (1-6) : "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid Combat Strength.")
    combatStrength = 1 #default value for invalid input

#Inputs combat strength monster
mCombatStrength= int(input("Enter monster's combat strength (1-6) : "))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid Monster Combat Strength.")
    mCombatStrength = 1 #default value for invalid input

# Simulate Battle rounds
for j in range(1, 21,2): #Simulation of 20 rounds, stepping by 2
    # Dice roll for hero and monster
    heroRoll= random.choice(diceOptions)
    monsterRoll= random.choice(diceOptions)

    # Weapons selected
    heroWeapon = weapons[heroRoll-1]
    monsterWeapon = weapons[monsterRoll-1]

    # calculate total strength
    heroTotal= combatStrength+ heroRoll
    monsterTotal= combatStrength+ monsterRoll

    #print round details
    print(f"\nRound {j} Hero rolled: {heroRoll} Monster rolled: {monsterRoll}")
    print(f"Hero selected: {heroWeapon}, Monster selected: {monsterWeapon}")
    print(f"Hero total: {heroTotal}, Monster total: {monsterTotal}")
