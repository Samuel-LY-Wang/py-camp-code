from random import randint
data={"rock":0, "paper":1, "scissors":2}
rev_data=["rock", "paper", "scissors"]
print("Welcome to Rock Paper Scissors!")
chosen=False
while not chosen:
    choice=input("What do you choose? (rock, paper, scissors)\n").lower()
    if choice in data:
        choice_num=data[choice]
        chosen=True
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")
computer_choice_num=randint(0,2)
print("The computer chose", rev_data[computer_choice_num] + ".")
if choice_num == computer_choice_num:
    print("It's a tie!")
elif (choice_num + 1) % 3 == computer_choice_num:
    print("You lose!")
else:
    print("You win!")