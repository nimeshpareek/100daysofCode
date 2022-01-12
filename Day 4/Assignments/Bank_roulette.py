
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length_of_list = len(names)
#x = int(0)
#print(length_of_list)
winner_index = random.randint(0, length_of_list-1)
#print(winner_index)
winner = names[winner_index]
print(winner + " is going to buy the meal today !")

