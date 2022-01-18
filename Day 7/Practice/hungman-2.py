import random

word_list = ["nimesh", "naresh", "kanishk"]
random_word = random.choice(word_list)
#print(random_word)

list_name = []
for x in random_word:
    list_name.append("_")

#print(list_name)
#user_input = input("Enter a letter to be guessed : ")
# for i in random_word:
#     if user_input == i:
#         print("Here i is: " + i)
#         for i in list_name:
#             i = user_input
#             print("entered in if condition")
count = 0
while count < len(random_word):
    user_input = input("GUESS LETTER-- : ")
    for i in range(len(random_word)):
        if user_input == random_word[i]:
            count = count + 1
            for guess in list_name:
                list_name[i] = user_input
                print(list_name)
                break

#print(list_name)


