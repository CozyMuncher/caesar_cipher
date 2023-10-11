while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decrypted_text = input("Decrypted Message:")
    encrypted_text = ""
    for char in decrypted_text:
        index = 0
        if (alphabet.index(char)+13) > 26:
            index = alphabet.index(char)+13 - 26
        else:
            index = alphabet.index(char)+13
        encrypted_text += alphabet[index]
    print(encrypted_text)
