#even elements
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [num for num in numbers if num % 2 == 0]
# with open("day26/even_numbers.txt", "w") as file:
#     for number in even_numbers:
#         file.write(f"{number}\n")
# with open("day26/even_numbers.txt", "r") as file:
#     even_numbers_from_file = file.readlines()
#     even_numbers_from_file = [int(num.strip()) for num in even_numbers_from_file]

# sentence="The quick brown fox jumps over the lazy dog"
# words= sentence.split()
# print(words)

#ACTUAL PROJECT: NATO Alphabet
word=input("Enter a word: ").upper()
nato_alphabet = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
    'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
    'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 
    'X': 'X-ray',  'Y': 'Yankee',  'Z':  "Zulu"
}
nato_word = []
while len(nato_word) == 0:
    try:
        nato_word = [nato_alphabet[letter] for letter in word]
        break
    except KeyError:
        print("Please enter a valid word containing only letters A-Z.")
        word = input("Enter a word: ").upper()

print(nato_word)