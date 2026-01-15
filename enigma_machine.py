# enigma machine project
# coded by oscar euceda
# date: dec 11, 2025
# file name = vigenereexample.txt

import os

# note to self - the modulo is used to iterate through each
# letter of the key and then "wrap around" to the first index once
# the length gets too large.
def vigenere(phrase, word_key, decrypt=False):
    # minimal fixes:
    # - keep non-letters unchanged
    # - only advance key index when a letter is encrypted/decrypted
    # - basic key validation
    if not word_key or not word_key.isalpha():
        print("[!] Key must contain only letters A-Z and cannot be empty.")
        return

    final_key_string = []
    final_key_decimals = []
    phrase_decimals = []
    rotation_list = []
    translation = []
    translation_string = ""
    decimal = []
    alphabet = []
    for letters in range(65, 91):
        alphabet.append(chr(letters))
        decimal.append(letters)

    key_index = 0  # <-- only increments when phrase character is alphabetic

    for letter in range(len(phrase)):
        ch = list(phrase.upper())[letter]

        # keep punctuation/spaces/numbers unchanged
        if not ch.isalpha():
            translation_string += ch
            continue

        phrase_decimals.append(decimal[alphabet.index(ch)])

        final_key_string.append(list(word_key.upper())[key_index % len(word_key)])
        final_key_decimals.append(decimal[alphabet.index(list(word_key.upper())[key_index % len(word_key)])])

        # encrypt/decrypt
        if not decrypt:
            rotation_list.append((final_key_decimals[key_index] + phrase_decimals[key_index]) % 26)
        else:
            rotation_list.append((phrase_decimals[key_index] - final_key_decimals[key_index]) % 26)

        translation.append(alphabet[rotation_list[key_index]])
        translation_string += translation[key_index]

        key_index += 1  # <-- advance key only after processing a letter

    print("Encoded Phrase -> ", translation_string)


def check_phrase(pre_phrase):
    print("Original phrase -> ", pre_phrase)
    return pre_phrase


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()


def menu():
    option = input("Welcome to the Enigma Machine!"
                   "\n\n<> VIGENERE CIPHER OPTIONS <>"
                   "\n[1] Encode a string"
                   "\n[2] Decode a string"
                   "\n[3] Encode a string inside a file"
                   "\n[4] Decode a string inside a file"
                   "\n Your Option: ")
    clear()

    if option in ("1", "2"):
        pre_phrase = input("Type in the phrase: ").upper()
        clear()
        phrase = check_phrase(pre_phrase)

        word_key = input("Type in the key: ").upper()
        # minimal error checking for key
        if not word_key or not word_key.isalpha():
            input("Key must contain only letters A-Z and cannot be empty. Press enter to continue... ")
            clear()
            return

        if option == "1":
            vigenere(phrase, word_key)
        elif option == "2":
            vigenere(phrase, word_key, decrypt=True)

        input("Press any key to return to menu...")
        clear()

    elif option in ("3", "4"):
        filename = input("Type in the filename: ")

        try:
            with open(filename, "r") as file:
                pre_phrase = file.read().upper()

            clear()
            if not pre_phrase.strip():
                input("File is empty. Press enter to continue... ")
                clear()
                return

            phrase = check_phrase(pre_phrase)

            word_key = input("Type in the key: ").upper()
            if not word_key or not word_key.isalpha():
                input("Key must contain only letters A-Z and cannot be empty. Press enter to continue... ")
                clear()
                return

            if option == "3":
                vigenere(phrase, word_key)
            elif option == "4":
                vigenere(phrase, word_key, decrypt=True)

            input("Press any key to return to menu...")
            clear()

        except FileNotFoundError:
            clear()
            input("File not found. Press enter to continue... ")
            clear()
        except Exception:
            clear()
            input("An error occurred:\nPress enter to continue... ")
            clear()

    else:
        input("Invalid option. Press enter to continue... ")
        clear()


if __name__ == '__main__':
    while True:
        menu()
