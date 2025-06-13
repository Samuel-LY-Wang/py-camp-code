from tkinter import *
from question_model import Question
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("The Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.q = quiz

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.update_question()

        true_img = PhotoImage(file="day34/images/true.png")
        false_img = PhotoImage(file="day34/images/false.png")
        self.true_button = Button(image = true_img, bg="green", fg="white", command=lambda: self.press("True"))
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image = false_img, bg="red", fg="white", command=lambda: self.press("False"))
        self.false_button.grid(row=2, column=1)

        self.score = Label(text="Score: 0", font=("Arial", 24, "bold"), bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.window.mainloop()
    def press(self, answer):
        is_correct = self.q.check_answer(answer)
        self.give_feedback(is_correct)
    def update_score(self, score):
        self.score.config(text=f"Score: {score}")
    def update_question(self):
        q_text = self.q.next_question()
        if q_text == "You've completed the quiz.":
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            return None
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.canvas.config(bg="white")
    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            print("Correct")
            self.update_score(self.q.score)
        else:
            self.canvas.config(bg="red")
            print("Incorrect")
        self.canvas.update()
        self.window.after(1000, lambda: self.update_question())