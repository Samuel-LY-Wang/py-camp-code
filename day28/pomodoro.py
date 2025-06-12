# IMPORTS
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)
checks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
checks.grid(column=1, row=3)

global reps
reps=0
global timer
timer=None
global timer_running
timer_running = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global timer_running
    global reps
    timer_running = False
    window.after_cancel(timer) # Cancel the countdown if it's running
    reps=0
    update_checks()
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    timer=None


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global timer
    global timer_running
    if timer is None:
        timer_running = True
    if timer_running:
        count_down(WORK_MIN * 60)
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    update_checks()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    global timer
    global timer_running
    if timer_running:
        canvas.itemconfig(timer_text, text=f"{time//60}:{time%60:02}")
        if time>0:
            timer=window.after(1000, count_down, time-1)
        else:
            start_timer()

#BUTTON SETUP
start_buttom = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_buttom.grid(column=0, row=2)
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
check_mark="✓"
def update_checks():
    global reps
    checks.config(text=check_mark * (reps // 2))

# Start the Tkinter event loop
window.mainloop()