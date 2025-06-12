import pandas as pd
import turtle
def load_data():
    data = pd.read_csv("day25/us-states-game/50_states.csv")
    return data
def create_state_dict(data):
    state_dict = {}
    for index, row in data.iterrows():
        state_dict[row["state"].lower()] = row["state"]
    return state_dict
def check_state(state, state_dict):
    if state.lower() in state_dict:
        return state_dict[state.lower()]
    else:
        return None
# US States Game
t=turtle.Turtle()
s=turtle.Screen()
s.title("US States Game")
s.setup(width=725, height=491)
img="day25/us-states-game/blank_states_img.gif"
s.bgpic(img)
t.hideturtle()
t.penup()
game_running=True
data=load_data()
state_dict = create_state_dict(data)
correct_guesses = []
while game_running:
    ans = s.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name? Type exit to end").strip()
    if ans == "exit":
        game_running = False
        continue
    state_name = check_state(ans, state_dict)
    if state_name and state_name not in correct_guesses:
        correct_guesses.append(state_name)
        t.goto(data[data["state"] == state_name]["x"].values[0], data[data["state"] == state_name]["y"].values[0])
        t.write(state_name, align="center", font=("Arial", 8, "normal"))
    elif state_name in correct_guesses:
        s.textinput(title="Already Guessed", prompt=f"You already guessed {state_name}. Try another one.")
    else:
        s.textinput(title="Not a State", prompt=f"{ans} is not a valid US state. Try again.")
    if len(correct_guesses) == 50:
        s.textinput(title="Congratulations!", prompt="You've guessed all the states! Press OK to exit.")
        game_running = False
#save missed states to CSV
list_of_states = data["state"].tolist()
missed_states = [state for state in list_of_states if state not in correct_guesses]
missed_states_dict = {"Missed States": missed_states}
missed_states_df = pd.DataFrame(missed_states_dict)
missed_states_df.to_csv("day25/us-states-game/missed_states.csv", index=False)
# Close the turtle graphics window
t.mainloop()