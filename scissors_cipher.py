while True:
    message = input("Decrypted / Encrypted message:")
    message_list = list(message)  # You can directly convert the input string to a list of characters
    even_letters = []
    encrypted = ''

    if len(message) % 2 == 0:
        for counter in range(0, len(message), 2):
            even_letters.append(message_list[counter])
        odd_letters = [message_list[i] for i in range(1, len(message), 2)]        

        for i in range(len(even_letters)):
            encrypted += odd_letters[i]
            encrypted += even_letters[i]

    else:
        for counter in range(0, len(message) - 1, 2):
            even_letters.append(message_list[counter])
        odd_letters = [message_list[i] for i in range(1, len(message) - 1, 2)]
        odd_letters.append(message[-1])

        for i in range(len(even_letters)):
            encrypted += odd_letters[i]
            encrypted += even_letters[i]

        encrypted += odd_letters[-1]

    print(encrypted)
