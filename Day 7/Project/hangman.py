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

word = "qwertyq"
lives = 0
count = 0
word_length = len(word)

display = []
for i in range(word_length):
    display += "_"

# user_input = input("Input: ")
# print(type(user_input))
# print(display)
# for x in range(word_length):
#     if word[x] == user_input:
#         print("Yes")
end_of_game = False
while not end_of_game:
    user_input = input("guess letter: ")
    for position in range(word_length):
        if word[position] == user_input:
            display[position] = word[position]

    print(display)
    print(hangman[lives])
    if user_input not in word:
        lives += 1
        print(lives)
    if lives == 7:
        end_of_game = True
        print("***** YOU LOSE ****")

    if "_" not in display:
        end_of_game = True
        print("***** YOU WIN *****")







