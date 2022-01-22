alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
plain_text = input("Type your message:\n").lower()
shifted_value = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# def encrypt(your_text, i):
#     for i in alphabet:
#         [i] = alphabet;


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt(your_text = text, i = shift)

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_letter = alphabet[position + shift]
        cipher_text = cipher_text + new_letter

    print(cipher_text)


def decrypt(shift, cipher_text):
    old_text = ""
    for letter in cipher_text:
        prev_position = alphabet.index(letter)
        old_letter = alphabet[prev_position - shift]
        old_text = old_text + old_letter
    print(old_text)


if direction == "encode":
    encrypt(text = plain_text, shift = shifted_value)
elif direction == "decode":
    decrypt(shift = shifted_value, cipher_text = plain_text)
else:
    print("wrong input!!")
