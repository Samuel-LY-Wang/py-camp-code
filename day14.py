#Higher or lower guessing game
#TODO: add game data
#TODO: add the logic from the actual higher or lower
#TODO: maybe add cool art if I feel like it
#no leaderboard because I don't have the capability to implement server-side storage
from higher_lower_data import data
import random

def get_random_account():
    """Get a random account from the data."""
    return random.choice(data)

score=0
print("Welcome to Higher or Lower!")
print("Guess who has more followers on Instagram. Data may be outdated, so tread cautiously.")
first_time=True
account_a = get_random_account()
account_b = get_random_account()
while account_a == account_b:
    account_b = get_random_account()
while True:
    if not first_time:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
    first_time = False
    print("\nCurrent score: {}".format(score))
    print("A: {}, a {} from {}".format(account_a['name'], account_a['description'], account_a['country']))
    print("B: {}, a {} from {}".format(account_b['name'], account_b['description'], account_b['country']))
    guess = input("Type 'A' or 'B': ").strip().upper()
    while guess not in ['A', 'B']:
        print("Invalid input. Please type 'A' or 'B'.")
        guess = input("Type 'A' or 'B': ").strip().upper()
    if (guess == 'A' and account_a['follower_count'] > account_b['follower_count']):
        print("Correct! {} has more followers than {}.".format(account_a['name'], account_b['name']))
        score += 1
        continue
    elif (guess == 'B' and account_b['follower_count'] > account_a['follower_count']):
        print("Correct! {} has more followers than {}.".format(account_b['name'], account_a['name']))
        score += 1
        continue
    else:
        print("Incorrect! {} has {} million followers, while {} has {} million followers.".format(account_a['name'], account_a['follower_count'], account_b['name'], account_b['follower_count']))
        break
print("Game over! Your final score is: {}".format(score))