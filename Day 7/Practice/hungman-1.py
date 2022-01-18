import random

word_list = ["nimesh", "naresh", "kanishk"]
word = random.choice(word_list)
user_input = input("Guess a letter: ")
word_length = len(word)

# for x in range(0, word_length - 1):
#      if word[x] == user_input:
#          print("right")
#      else:
#          print("Wrong")

for x in word:  # both loops works fine we can use any of them
    if x == user_input:
        print("right")
    else:
        print("Wrong")

