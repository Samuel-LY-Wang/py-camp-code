counter=0
# basic state machine
# states: 0=failed, 1=beginning, 2=looking, 3=mountain, 4=lake, 5=bank, 6=muscled out, 7=paid, 8=split
cur_state=1
print(
    '''You have a candy bar in your pocket.
    Do you try to open it or look for help?'''
)
while cur_state != 0 and cur_state < 6:
    user_input = input(">").lower()
    if cur_state == 1:
        valid_options=["open", "open it", "try again", "help", "look for help"]
        if user_input in valid_options:
            if user_input == "open" or user_input == "open it" or user_input == "try again":
                if (counter < 5):
                    print("You try and open the candy bar but fail.")
                    counter += 1
                    print("Do you try again or look for help?")
                else:
                    print("After several attempts, you give up on opening the candy bar.")
                    print("You decide to go to the gym and train your arms")
                    print("After a few hours, you are strong enough to open the candy bar.")
                    print("You have achieved the muscled-out ending.")
                    cur_state = 6
            else:
                print("Where do you look? The mountain, the lake, or the bank?")
                cur_state = 2
                continue
        else:
            print("Invalid option. Try again.")
    elif cur_state == 2:
        valid_options = ["mountain", "lake", "bank"]
        if user_input in valid_options:
            if user_input == "mountain":
                print("You tried climbing the mountain. It was too steep, and you fell.")
                print("where else do you look?")
                cur_state = 3
                continue
            elif user_input == "lake":
                print("You found one of your friends by the lake.")
                print("They offer to help, but they want to split the candy bar.")
                print("Do you accept? (y/n)")
                cur_state = 4
                continue
            else:
                print("The teller offers to help you, but there is a price to pay.")
                print("The price is $5 and a subscription to the bank's newsletter.")
                print("Do you pay the price of $5 and your dignity? (y/n)")
                cur_state = 5
                continue
        else:
            print("Invalid option. Try again.")
    elif cur_state == 3:
        valid_options = ["lake", "bank"]
        if user_input in valid_options:
            if user_input == "lake":
                print("You found one of your friends by the lake.")
                print("They offer to help, but they want to split the candy bar.")
                print("Do you accept? (y/n)")
                cur_state = 4
                continue
            else:
                print("The teller offers to help you, but there is a price to pay.")
                print("The price is $5 and a subscription to the bank's newsletter.")
                print("Do you pay the price of $5 and your dignity? (y/n)")
                cur_state = 5
                continue
        elif user_input == "mountain":
            print("Despite your previous failed attempt, you tried climbing the mountain again.")
            print("However, the mountain was too steep, and you died trying to climb it.")
            print("You have failed to eat the delicious candy.")
            cur_state = 0
        else:
            print("Invalid option. Try again.")
    elif cur_state == 4:
        valid_options = ["y", "n"]
        if user_input in valid_options:
            if user_input == "y":
                print("Together, with the power of friendship, you opened the candy bar.")
                print("As promised, you split the candy bar with your friend.")
                print("You have achieved the split ending.")
                cur_state = 8
            else:
                print("You try alone to open the candy bar.")
                print("However, the stupid wrapper is too tough.")
                print("You did not open the candy bar, and have failed.")
                cur_state = 0
        else:
            print("Invalid option. Try again.")
    elif cur_state == 5:
        valid_options = ["y", "n"]
        if user_input in valid_options:
            if user_input == "y":
                print("You were ready to pay $5 for the candy bar, but your email was too far for a simple piece of sugar and chocolate.")
                print("But you were very hungry, so you swallowed your pride and paid the price.")
                print("You have achieved the paid ending.")
                cur_state = 7
            else:
                print("The teller tells you to get out of the bank.")
                print("You did not open the candy bar, and have failed.")
                cur_state = 0
        else:
            print("Invalid option. Try again.")