alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
plain_text = input("Type your message:\n").lower()
shifted_value = int(input("Type the shift number:\n"))


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
