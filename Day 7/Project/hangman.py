import random

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print(hangman[0])
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
life_count == 0
while count < len(random_word) or life_count == 6:
    user_input = input("GUESS LETTER-- : ")
    for i in range(len(random_word)):
        if user_input == random_word[i]:
            count = count + 1
            for guess in list_name:
                list_name[i] = user_input
                print(list_name)
                print(hangman[life_count])
                break
        else:
            life_count = life_count + 1
            print(hangman[life_count])


print(hangman[life_count])


#print(list_name)


