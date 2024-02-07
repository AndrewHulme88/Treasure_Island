print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print("Welcome to Treasure Island!")
print("You arrive on the beach and take a look around.")
print("Ahead of you is a dense jungle. To your right, there looks like a shipwreck on the beach. To your left, there is a steep cliff.")
path_1 = input("Which way would you like to go? J (Jungle) S (Shipwreck) or C (Cliff)\n").upper()

if path_1 == "J":
    print("You venture forth into the jungle.")

    print("After slogging through the dense terrain for hours, you come across a temple.")
    print("Will you enter the temple, or turn back?")
    path_2 = input("T (Temple) or B (Back)\n").upper()

    if path_2 == "T":
        print("You enter the temple, slowly descending into darkness.")

        print("You come to a semi lit room with three chests.")
        print("Chest 1 is adorned with gold. Chest 2 is covered in rubies. Chest 3 has a Python wrapped around it.")
        path_3 = input("1 (chest 1), 2 (chest 2), 3 (chest 3)\n").upper()

        if path_3 == "1":
            print("You approach the golden chest. As you reach out, you feel cold. Your hand touches the chest. All of a sudden you begin to turn to gold. Eventually you are completely encased in gold for the rest of time...")
            print("GAME OVER!")
        elif path_3 == "2":
            print("You attempt to open the ruby covered chest. As you lift the chest you see a bright light within. You fully lift the lid, staring into the light. Suddenly everything goes black. You are left to wander blindly through the temple until your final day.")
            print("GAME OVER!")
        elif path_3 == "3":
            print("You approach the third chest. The python wrapped around it stares at you intently. You open the chest. It is full of riches beyond your wildest dreams. The python tells you you have completed the trial of the temple.")
            print("You sail away form Treasure Island, with a chest full of treasure and a strange talking python for company.")
            print("YOU WIN!!")
        else:
            print("GAME OVER!")
    elif path_2 == "B":
        print("You walk for hours, but it seems as though you have lost your way.")
        print("Darkness begins to fall, and you hear the sounds of the creatures of the night as they begin to stir.")
        print("Suddenly, a giant python wraps itself around you. Moments later, it begins to devour your crushed, lifeless body...")
        print("GAME OVER!")
    else:
        print("GAME OVER!")

elif path_1 == "S":
    print("You aproach the shipwreck, only to be ambushed by pirates!")
    print("GAME OVER!")
elif path_1 == "C":
    print("You start to climb the cliff. At first it seems easy enough. You are almost at the top when you loose your grip and plummet to a splattery death!")
    print("GAME OVER!")
else:
    print("GAME OVER!")