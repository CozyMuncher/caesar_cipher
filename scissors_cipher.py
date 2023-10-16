"""A cipher wich encrypt words by switching adjacent letters"""

while True:
    message = input("Decrypted / Encrypted message:")
    message_list = list(message)  # convert the input string to a list of characters
    even_letters = []
    ENCRYPTED = ''

    if len(message) % 2 == 0:
        for counter in range(0, len(message), 2):
            even_letters.append(message_list[counter])
        odd_letters = [message_list[i] for i in range(1, len(message), 2)]

        for i in enumerate(len(even_letters)):
            ENCRYPTED += odd_letters[i]
            ENCRYPTED += even_letters[i]

    else:
        for counter in range(0, len(message) - 1, 2):
            even_letters.append(message_list[counter])
        odd_letters = [message_list[i] for i in range(1, len(message) - 1, 2)]
        odd_letters.append(message[-1])

        for i in enumerate(len(even_letters)):
            ENCRYPTED += odd_letters[i]
            ENCRYPTED += even_letters[i]

        ENCRYPTED += odd_letters[-1]

    print(ENCRYPTED)
