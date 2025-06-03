def encode(s, shift):
    encoded = []
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - base + shift) % 26 + base)
            encoded.append(encoded_char)
        else:
            encoded.append(char)
    return ''.join(encoded)
def decode(s, shift):
    encoded = []
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - base - shift) % 26 + base)
            encoded.append(encoded_char)
        else:
            encoded.append(char)
    return ''.join(encoded)

while True:
    print("Welcome to the Caesar Cipher Program!")
    choice= input("Do you want to (e)ncode or (d)ecode a message? ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encode or 'd' to decode.")
        continue
    if choice == 'e':
        message = input("Enter the message to encode: ")
        shift = int(input("Enter the shift value (1-25): "))
        if shift < 1 or shift > 25:
            print("Shift value must be between 1 and 25.")
            continue
        encoded_message = encode(message, shift)
        print(f"Encoded message: {encoded_message}")
        while True:
            again=input("Do you want to go again? (y/n): ").lower()
            if again not in ['y', 'n']:
                print("Invalid choice. Please enter 'y' to continue or 'n' to exit.")
            elif again == 'y':
                break
            else:
                exit()
            
    else:
        message = input("Enter the message to decode: ")
        shift = int(input("Enter the shift value (1-25): "))
        if shift < 1 or shift > 25:
            print("Shift value must be between 1 and 25.")
            continue
        decoded_message = decode(message, shift)
        print(f"Decoded message: {decoded_message}")
        while True:
            again=input("Do you want to go again? (y/n): ").lower()
            if again not in ['y', 'n']:
                print("Invalid choice. Please enter 'y' to continue or 'n' to exit.")
            elif again == 'y':
                break
            else:
                exit()