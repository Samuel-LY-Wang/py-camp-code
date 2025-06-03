#silent auction
# import os
# import sys
def clear_console():
    # if sys.platform.startswith('win'):
    #     os.system('cls')  # For Windows
    # else:
    #     os.system('clear')  # For Linux and macOS
    print("\n" * 100)  # works well enough I guess
bids={}
print("Welcome to the silent auction!")
item=input("What item is bring auctioned?\n")
while True:
    name=input("What is your name? ")
    bid=float(input(f"What will you bid on {item}? $"))
    bids[name]=bid
    more=input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more == 'yes':
        clear_console()
    else:
        print("Bidding has ended.")
        break
clear_console()
highest_bidder = max(bids, key=bids.get)
highest_bid = bids[highest_bidder]
print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")
print(f"Congrats to {highest_bidder} for winning the auction for {item}!")