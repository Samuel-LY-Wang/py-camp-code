from question_model import Question
from data import get_questions
from ui import QuizInterface
from quiz_brain import QuizBrain
import json
import time
from tkinter import *

global max_qs
max_qs = 20 # default if the window is closed or fails to appear

setup = Tk()
setup.title("Setup")
setup.minsize(width=250,height=250)
text = Label(text="Enter the number of questions you wish to do")
text.grid(row=0,column=0)
entry = Entry(width=20)
entry.focus()
entry.grid(row=1,column=0)
def get_input_val(event=None):
    global max_qs
    max_qs = entry.get()
    try:
        max_qs = int(max_qs)
    except TypeError:
        raise Exception("You must enter an integer!")
    assert 1<=max_qs<=50
    setup.destroy()
entry.bind("<Return>", get_input_val)
setup.mainloop()

question_bank = []
question_data = get_questions(max_qs)
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

while quiz.still_has_questions():
    time.sleep(1)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

#save score info to json
try:
    score_data=json.load(open("day34/scores.json"))
except FileNotFoundError:
    score_data = {}
score_data[str(time.time())] = {"score": quiz.score, "questions": max_qs, "percent": float(quiz.score)/float(max_qs)*100}
json.dump(score_data, open("day34/scores.json", "w"), indent=4)