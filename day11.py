import random

suits=["C","D","H","S"]
values=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
deck=[f"{value}{suit}" for suit in suits for value in values]*8 # 8 standard decks combined as per casino rules
def deal_card():
    if not deck:
        return None
    card = random.choice(deck)
    deck.remove(card)
    return card
def deal_hand(num_cards):
    hand=[]
    for _ in range(num_cards):
        card = deal_card()
        if card is None:
            break
        hand.append(card)
    return hand
def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        value = card[:-1]  # Get the value part of the card (e.g., '10', 'J', 'Q', etc.)
        if value in ['J', 'Q', 'K']:
            score += 10
        elif value == 'A':
            aces += 1
            score += 11  # Initially count Ace as 11
        else:
            score += int(value)  # Convert numeric values to int
    while score > 21 and aces:
        score -= 10  # Adjust for Ace being counted as 1 instead of 11
        aces -= 1
    return score
def has_blackjack(hand):
    return len(hand) == 2 and calculate_score(hand) == 21
print("Welcome to Blackjack!")
print("Please note that suits are represented as follows:")
print('''C=Clubs
D=Diamonds
H=Hearts
S=Spades
''')
print("Values are represented as follows:")
print('''2-10 represent themselves
J=Jack (value 10)
Q=Queen (value 10)
K=King (value 10)
A=Ace (value can be chosen as 1 or 11)
''')
dealer_hand=deal_hand(2)
player_hand=deal_hand(2)
print(f"Dealer's hand: {dealer_hand[0]}")
print(f"Player's hand: {player_hand}")
if has_blackjack(player_hand):
    print("Player has a Blackjack! Player wins!")
    exit()
if has_blackjack(dealer_hand):
    print("Dealer has a Blackjack! Dealer wins!")
    exit()
while calculate_score(dealer_hand) < 17:
    dealer_hand.append(deal_card())
while True:
    more_cards = input("Do you want to draw another card? (yes/no): ").strip().lower()
    if more_cards == 'yes':
        player_hand.append(deal_card())
        print(f"Player's hand: {player_hand}")
        if calculate_score(player_hand) > 21:
            print("Player busts! Dealer wins.")
            break
    elif more_cards == 'no':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)
print(f"Player's final hand: {player_hand} (Score: {player_score})")
print(f"Dealer's final hand: {dealer_hand} (Score: {dealer_score})")
if dealer_score > 21:
    print("Dealer busts! Player wins.")
else:
    if player_score > dealer_score:
        print("Player wins!")
    elif dealer_score > player_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")