while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_text = ''
    decrypted_text = input("Decrypted Text:")
    key = input("Key:")
    iter = 0

    for char in decrypted_text:
        index = key[iter]
        temp = 0
        if (alphabet.index(char)+alphabet.index(index)) > 26:
            temp = alphabet.index(char)+alphabet.index(index) - 26
        else:
            temp = alphabet.index(char)+alphabet.index(index)
        encrypted_text += alphabet[temp]
        iter += 1
        if iter > len(key)-1:
            iter = 0

    print(encrypted_text)
