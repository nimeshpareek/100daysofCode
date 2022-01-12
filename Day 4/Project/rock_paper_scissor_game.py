import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_input = input("Enter Your Choice !!! \nRock, Paper or Scissor\nFor Rock press 1\nFor Paper press 2\n"
                   "For Scissor press 3 : ")
if user_input == '1':
    print("Your Choice is: ROCK")
    print(rock)
elif user_input == '2':
    print("Your Choice is: PAPER")
    print(paper)
elif user_input == '3':
    print("Your Choice is: SCISSOR")
    print(scissor)
else:
    print("Wrong input :")


random_value = random.randint(1, 3)
int_user_input = int(user_input)

print("-----------------------------------------------")
if random_value == 1:
    print("Opponent Choice is ROCK")
    print(rock)
elif random_value == 2:
    print("Opponent Choice is PAPER")
    print(paper)
else:
    print("Opponent Choice is SCISSOR")
    print(scissor)

if random_value == int_user_input:
    print(" *******TIE*******")
elif int_user_input == 1 and random_value == 2:
    print("*****YOU LOSE*****")
elif int_user_input == 1 and random_value == 3:
    print("YOU WON!!!")
elif int_user_input == 2 and random_value == 1:
    print("YOU WON")
elif int_user_input == 2 and random_value == 3:
    print("YOUR LOSE")
elif int_user_input == 3 and random_value == 1:
    print("YOUR LOSE")
elif int_user_input == 3 and random_value == 2:
    print("YOU LOSE")
else:
    print("this code is not working")
