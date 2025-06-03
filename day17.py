from quiz_data import question_data
from random import shuffle

class Question:
    def __init__(self, question: str, answer: bool):
        self.question = question
        self.answer = bool(answer)
    def __str__(self):
        return f"Question: {self.question}\nAnswer: {self.answer}"
    def ask(self):
        print(self.question)
    def is_correct(self, response: bool):
        return self.answer == response
questions=[]
for question in question_data:
    q = Question(question["text"], question["answer"])
    questions.append(q)
shuffle(questions)
print("This is the True/False Quiz.")
score=0
for question in questions:
    question.ask()
    response = None
    while response not in [True, False]:
        response = input("True or False? ").strip().lower()
        if response == "true" or response=="t":
            response = True
        elif response == "false" or response=="f":
            response = False
        else:
            print("Invalid response. Please answer with 'True' or 'False'.")
            continue
    if question.is_correct(response):
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
print(f"Your final score is {score}/{len(questions)}.")