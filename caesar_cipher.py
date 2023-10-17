"""A program to encode a given message using Caesar Cipher and a key"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    decrypted_text = input("Decrypted Message:")
    key = int(input("Key:"))

    ENCRYPTED_TEXT = ""

    for char in decrypted_text:

        # Checks if character is a special character
        if char not in alphabet:
            ENCRYPTED_TEXT += char
        else:

            # Checks if the index is greater than 26
            # or less than 0 and changes the index accordingly
            INDEX = 0
            if (alphabet.index(char)+key) > 26:
                INDEX = alphabet.index(char)+key - 26
            else:
                INDEX = alphabet.index(char)+key

            ENCRYPTED_TEXT += alphabet[INDEX]

    print(ENCRYPTED_TEXT)
