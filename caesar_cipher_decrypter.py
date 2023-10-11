alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypted_text = input("Encrypted Message:")
key = int(input("Key:"))
decrypted_text = ""
for char in encrypted_text:
    index = 0
    if (alphabet.index(char)-key) < 0:
        index = alphabet.index(char)-key + 26
    else:
        index = alphabet.index(char)-key
    decrypted_text += alphabet[index]
print(decrypted_text)
