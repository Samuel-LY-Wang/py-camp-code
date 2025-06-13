from question_model import Question
from data import question_data
from ui import QuizInterface
from quiz_brain import QuizBrain
import json
import time
from tkinter import *

setup = Tk()
text = Label(text="Enter the number of questions you wish to do")
entry = Entry()
entry.bind("<Return>", lambda: get_input_val())
def get_input_val():
    max_qs = entry.get()
    try:
        max_qs = int(max_qs)
    except TypeError:
        raise Exception("You must enter an integer!")
    assert 1<=max_qs<=50
setup.mainloop()

question_bank = []
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
score_data[str(time.time())] = {"score": quiz.score, "questions": max_qs, }
json.dump(score_data, open("day34/scores.json", "w"), indent=4)