import random
def generate_password(length=12, num_uppercase=2, num_lowercase=2, num_numbers=2, num_symbols=2):
    # Generates a random password with specified length
    # Also includes a required amount of uppercase letters, lowercase letters, numbers, and symbols
    if length < (num_uppercase + num_lowercase + num_numbers + num_symbols):
        raise ValueError("Total length must be at least the sum of all character types.")
    if num_uppercase < 0 or num_lowercase < 0 or num_numbers < 0 or num_symbols < 0:
        raise ValueError("Character counts must be non-negative.")
    symbols = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/"]
    
    # Generate random characters based on the specified counts
    password_chars = [
        chr(random.randint(65, 90)) for _ in range(num_uppercase)  # Uppercase letters A-Z
    ] + [
        chr(random.randint(97, 122)) for _ in range(num_lowercase)  # Lowercase letters a-z
    ] + [
        str(random.randint(0, 9)) for _ in range(num_numbers)  # Numbers 0-9
    ] + [
        random.choice(symbols) for _ in range(num_symbols)  # Random symbols from the list
    ]
    
    # Shuffle the characters to randomize their order
    random.shuffle(password_chars)
    
    # If the total length is less than specified, fill with random characters
    while len(password_chars) < length:
        password_chars.append(random.choice(symbols + [chr(random.randint(65, 90)), chr(random.randint(97, 122)), str(random.randint(0, 9))]))
    
    # Join the characters to form the password
    password = ''.join(password_chars[:length])
    
    return password