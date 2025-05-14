alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# def decrypt(original_text, shift_amount):
#     decipher_text = ""
#     for letter in original_text:
#         shift_position_backwards = alphabet.index(letter) - shift_amount
#         shift_position_backwards %= len(alphabet)
#         decipher_text += alphabet[shift_position_backwards]
#     print(f"Here is the decoded result: {decipher_text}")


# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")


def caesar(enc_dec, original_text, shift_amount):
    if enc_dec == "encode":
        cipher_text = ""
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")
    elif enc_dec == "decode":
        decipher_text = ""

        for letter in original_text:
            if letter not in alphabet:
                decipher_text += letter
            else:
                shift_position_backwards = alphabet.index(letter) - shift_amount
                shift_position_backwards %= len(alphabet)
                decipher_text += alphabet[shift_position_backwards]
        print(f"Here is the decoded result: {decipher_text}")
    else:
        print("That is not an option")




#
# encrypt(original_text=text, shift_amount=shift)
# decrypt(text,shift)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(direction, text, shift)

try_again = "yes"

while try_again == "yes":

    try_again = input("Do you want to play again? [yes/no]: ").lower()
    if try_again == "no":
        print("thanks for playing!")
        break

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)


