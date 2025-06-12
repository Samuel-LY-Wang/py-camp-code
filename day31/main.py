# Very rough code outline
# add a flashcard class (2x3 grid, columns 0-2, rows 0-1)
# add buttons for check and cross
# check should remove the card from the available deck (as a csv)
# cross should just get a new card
# if all cards are done, show a popup and reset the deck
import pandas as pd
from tkinter import *
from tkinter import messagebox
import random

#var setup
card_list = pd.read_csv("day31/ZhEnTranslations.csv").to_dict(orient="records")
#card_list = list of dicts {'中文': (chinese), 'English': (english)}
global available_cards
try:
    available_cards = pd.read_csv("day31/availablecards.csv").to_dict(orient="records")
    df= pd.DataFrame(available_cards)
    df.to_csv("day31/availablecards.csv", index=True, header=True, columns=["中文", "English"])
except FileNotFoundError:
    available_cards = card_list.copy()  # If no file exists, use the full card list
    df= pd.DataFrame(available_cards)
    df.to_csv("day31/availablecards.csv", index=True, header=True, columns=["中文", "English"])
# print(available_cards)
BG_COLOR= "#B1DDC6"

# UI setup
window = Tk()
window.title("Chinese-English Flashcards")
window.config(padx=50, pady=50, bg=BG_COLOR)
messagebox.showinfo(title="Welcome", message="Welcome to the Chinese Flashcard tool!\n\nPlease note that the translations come from Google Translate, with minimal human editing\nTHIS IS NOT A LANGUAGE LEARNING TOOL")

#canvas setup
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=3)
card_front = PhotoImage(file="day31/images/card_front.png")
card_back = PhotoImage(file="day31/images/card_back.png")
global card
card = random.choice(available_cards)
canvas.create_image(400, 263, image=card_front)
lang=canvas.create_text(400, 150, text="中文", font=("Arial", 40, "italic"), fill="black")
word=canvas.create_text(400, 263, text=card["中文"], font=("Arial", 60, "bold"), fill="black")

#canvas update
def update_canvas():
    """Update the canvas with the current card."""
    """called AFTER new card selected"""
    global card
    canvas.create_image(400, 263, image=card_front)
    canvas.create_text(400, 150, text="中文", font=("Arial", 40, "italic"), fill="black")
    canvas.create_text(400, 263, text=card["中文"], font=("Arial", 60, "bold"), fill="black")

#button functions
def reset_deck():
    """Reset the deck of available cards."""
    global available_cards
    available_cards = card_list.copy()
    df= pd.DataFrame(available_cards)
    df.to_csv("day31/availablecards.csv", index=True, header=True, columns=["中文", "English"])
    messagebox.showinfo(title="Deck Reset", message="The deck has been reset. You can start again.")

def get_new_card(old_card, iscorrect=False):
    """Get a new card from the available cards."""
    global available_cards
    global card
    if iscorrect:
        available_cards.remove(old_card)
        # messagebox.showinfo(title="Correct!", message="Great job! You got it right!")
        # popup was getting a bit annoying
    if not available_cards:
        messagebox.showinfo(title="No Cards Left", message="All cards have been used. Resetting the deck.")
        reset_deck()
        return get_new_card()  # Get a new card after resetting
    card = random.choice(available_cards)
    update_canvas()
    df= pd.DataFrame(available_cards)
    df.to_csv("day31/availablecards.csv", index=True, header=True, columns=["中文", "English"])

def flip_card():
    """Flip the card to show the English translation."""
    global card
    canvas.delete("all")  # Clear the canvas
    canvas.create_image(400, 263, image=card_back)
    canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"), fill="black")
    canvas.create_text(400, 263, text=card["English"], font=("Arial", 60, "bold"), fill="black")

#button setup
right= PhotoImage(file="day31/images/right.png")
wrong= PhotoImage(file="day31/images/wrong.png")
check_button = Button(image=right, command=lambda: get_new_card(card, iscorrect=True))
check_button.grid(column=0, row=1)
flip_button= Button(text="Flip", command=flip_card)
flip_button.grid(column=1, row=1)
cross_button = Button(image=wrong, command=lambda: get_new_card(card))
cross_button.grid(column=2, row=1)

window.mainloop()