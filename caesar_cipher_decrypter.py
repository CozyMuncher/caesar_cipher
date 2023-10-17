"""A program to decrypt text in Caesar Cipher with a given key"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    encrypted_text = input("Encrypted Message:")
    key = int(input("Key:"))

    DECRYPTED_TEXT = ""
    for char in encrypted_text:

        # Checks if the character is a special char
        if char not in alphabet:
            DECRYPTED_TEXT += char

        else:
            INDEX = 0

            # Checks if the index is greater than 26
            # or less than 0 and changes the index accordingly
            if (alphabet.index(char)-key) < 0:
                INDEX = alphabet.index(char)-key + 26
            else:
                INDEX = alphabet.index(char)-key

            # Adds the new character
            DECRYPTED_TEXT += alphabet[INDEX]
    print(f"Decrypted Text: {DECRYPTED_TEXT}")
