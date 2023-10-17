"""A cipher wich encrypt words by switching adjacent letters"""
text = input('Text to encrypt:')
char = list(text)
encrypted_char = []

last_letter = ''
if int(len(text) % 2) != 0:
    print('removing last digit')
    last_letter = char[-1]
    del char[-1]
    print(text)

for counter in range(0, int(len(char)/2)):
    encrypted_char.append(char[1])
    encrypted_char.append(char[0])
    del char[1]
    del char[0]

print(''.join(encrypted_char)+last_letter)
