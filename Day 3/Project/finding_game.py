print (
    '''
                                                                        
    |||||||||8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
       88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
       88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
       88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
       "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                 '''
)
name = input ("Please Enter your Name : ")
upper_name = name.upper ()
print (f"HEY {upper_name} WELCOME TO TREASURE HUNT GAME: ")

print ("Your mission is to find a treasure in this game :)) ")
choice1 = input (
    "you are at a crossroad where you want to go now if left then type left or is right type right :))>>"
).lower ()

if choice1 == "left":
    choice2 = input (
        "You have come to a lake. There is an island in the middle of the lake."
        " Type wait to wait for the boat: >> or type swim to swim across"
    ).lower ()
if choice2 == "wait":
    choice3 = input (
        "You arrived at an island unharmed. There is a house with 3 doors. one "
        "red one yellow and one blue so choose one  >> "
    ).lower ()
if choice3 == "red":
    print ("It's a room full of fire. Game over")
elif choice3 == "yellow":
    print ("You found the treasure. YOU WIN!!! HUREE!!!")
elif choice3 == "blue":
    print ("You enter a room of tiger, Game Over")
