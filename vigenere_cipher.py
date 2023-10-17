"""A program to encrypt and decrypt a message using vigenere cipher with a given key"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:

    ENCRYPTED_TEXT = ''
    decrypted_text = input("Decrypted Text:").lower()
    key = input("Key:").lower()

    ITERATION = 0

    for char in decrypted_text:

        # If character is not an alphabet, dont do stuff on it
        if char not in alphabet:
            ENCRYPTED_TEXT += char

        # Basically this is a caesar cipher
        # But uses two things
        # One is the current character in the decrypted text
        # It rotates the cipher based on its index
        # Then, the current character of the key,
        # The character is chosen based on the above caesar cipher
        # and choses the character with the current character of the key

        # Assuming the word is ION and the key is Hail
        # The index of I is 8
        # Thus, the code will use a caesar cipher with the characters being
        # offset by 8 steps.
        # The index of H is 7.
        # So, it will get the 7th character of the above cipher, which is P

        else:

            # Gets the current character of the key
            index = key[ITERATION]

            TEMP_INDEX = 0

            # Uses caesar cipher
            if (alphabet.index(char)+alphabet.index(index)) > 26:
                TEMP_INDEX = alphabet.index(char)+alphabet.index(index) - 26
            else:
                TEMP_INDEX = alphabet.index(char)+alphabet.index(index)

            # Gets the encrypted char
            ENCRYPTED_TEXT += alphabet[TEMP_INDEX]
            
            ITERATION += 1
            if ITERATION > len(key)-1:
                ITERATION = 0

    print(ENCRYPTED_TEXT)
