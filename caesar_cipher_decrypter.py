"""A program to decrypt text in Caesar Cipher with a given key"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    encrypted_text = input("Encrypted Message:")
    key = int(input("Key:"))
    DECRYPTED_TEXT = ""
    for char in encrypted_text:
        if char not in alphabet:
            DECRYPTED_TEXT += char
        else:
            INDEX = 0
            if (alphabet.index(char)-key) < 0:
                INDEX = alphabet.index(char)-key + 26
            else:
                INDEX = alphabet.index(char)-key
            DECRYPTED_TEXT += alphabet[INDEX]
    print(f"Decrypted Text: {DECRYPTED_TEXT}")
