from random import randint, choice, sample, shuffle
symbols=["`","~","!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]",":",";","'","\"","<",">",",",".","?","/"]
num_uppercase=int(input("How many uppercase letters would you like in your password?\n"))
num_lowercase=int(input("How many lowercase letters would you like in your password?\n"))
num_numbers=int(input("How many numbers would you like in your password?\n"))
num_symbols=int(input("How many symbols would you like in your password?\n"))
password_chars=[]
for i in range(num_uppercase):
    password_chars.append(chr(randint(65, 90)))  # Uppercase letters A-Z
for i in range(num_lowercase):
    password_chars.append(chr(randint(97, 122)))  # Lowercase letters a-z
for i in range(num_numbers):
    password_chars.append(str(randint(48, 57)))  # Numbers 0-9
for i in range(num_symbols):
    password_chars.append(choice(symbols))  # Random symbols from the list
shuffle(password_chars)  # Shuffle the characters to randomize their order
password=''.join(password_chars)  # Join the characters to form the password
print(f"Your password is: {password}")