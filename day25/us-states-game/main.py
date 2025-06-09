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
img="day25/us-states-game/blank_states_img.gif"
s.addshape(img)
t.hideturtle()
t.penup()


s.exitonclick()