"""A program to encrypt and decrypt a message using vigenere cipher with a given key"""

while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ENCRYPTED_TEXT = ''
    decrypted_text = input("Decrypted Text:").lower()
    key = input("Key:").lower()
    ITERATION = 0

    for char in decrypted_text:
        if char not in alphabet:
            ENCRYPTED_TEXT += char
        else:
            index = key[ITERATION]
            TEMP_INDEX = 0
            if (alphabet.index(char)+alphabet.index(index)) > 26:
                TEMP_INDEX = alphabet.index(char)+alphabet.index(index) - 26
            else:
                TEMP_INDEX = alphabet.index(char)+alphabet.index(index)
            ENCRYPTED_TEXT += alphabet[TEMP_INDEX]
            ITERATION += 1
            if ITERATION > len(key)-1:
                ITERATION = 0

    print(ENCRYPTED_TEXT)
