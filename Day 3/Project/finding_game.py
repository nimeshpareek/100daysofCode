print(
    '''

    |||||||||8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,
       88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8
       88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88
       88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88
       "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88
                                                                 '''
)
name = input("Please Enter your Name : ")
upper_name = name.upper()
print(f"HEY {upper_name} WELCOME TO TREASURE HUNT GAME: ")

print("Your mission is to find a treasure in this game :)) ")
choice1 = input(
    "you are at a crossroad where you want to go now if left then type left or is right type right :))>>"
).lower()

if choice1 == "left":
    choice2 = input(
        "You have come to a lake. There is an island in the middle of the lake."
        " Type wait to wait for the boat: >> "
    ).lower()
    if choice2 == "wait":
        choice3 = input(
        "You arrived at an island unharmed. There is a house with 3 doors. one "
        "red one yellow and one blue so choose one  >> "
         ).lower()
        if choice3 == "red":
             print("It's a room full of fire, Gmae Over!!!")
        elif choice3 == "Yellow":
             print("You found the treasure, YOU WIN!!!")
        elif choice3 == "blue":
            print("You enter the room of beasts. Game Over!!!")
        else:
            print("You chose the door which is close")
    else:
        print("You entered wrong input >>>>")
else:
    print("You fall into a hole. You LOSE~~~!!")       


