#Hangman
import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
HANGMANPICS.reverse()
file_words = open('10k-English-words.txt')
list_of_words = file_words.read().splitlines()
file_words.close()
word=random.choice(list_of_words)
l=len(word)
guessed=[False]*l
already_guessed = []
lives=6
print("Welcome to Hangman!")
while True:
    print(HANGMANPICS[lives])
    print(f"Word: {' '.join(['_' if letter not in already_guessed else letter for letter in word])}")
    print(f"Lives left: {lives}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue
    
    if guess in already_guessed:
        print("You have already guessed that letter.")
        continue
    
    already_guessed.append(guess)
    
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
        for i in range(l):
            if word[i]==guess:
                guessed[i]=True
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        lives -= 1
    
    if all(guessed):
        print(f"Congratulations! You've guessed the word: {word}")
        print(HANGMANPICS[lives])
        break
    
    if lives == 0:
        print("Oops, you failed")
        print(HANGMANPICS[lives])
        print(f"The word was: {word}")
        break