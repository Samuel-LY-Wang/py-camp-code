import random
guessing_range=[1,1000]
easy_guesses=20
hard_guesses=10

num=random.randint(guessing_range[0], guessing_range[1])
def check_guess(guess, num):
    if guess < num:
        return "Too low."
    elif guess > num:
        return "Too high."
    else:
        return "Correct!"
def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return easy_guesses
    elif difficulty == 'hard':
        return hard_guesses
    else:
        print("Invalid choice. Defaulting to easy.")
        return easy_guesses
def play_game():
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {guessing_range[0]} and {guessing_range[1]}.")
    
    guesses_left = choose_difficulty()
    
    while guesses_left > 0:
        print(f"You have {guesses_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        result = check_guess(guess, num)
        print(result)
        
        if result == "Correct!":
            print("Congratulations! You've guessed the number!")
            return
        
        guesses_left -= 1
    
    print(f"Sorry, you've run out of guesses. The number was {num}.")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break