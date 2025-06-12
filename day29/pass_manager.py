from tkinter import *
from tkinter import messagebox
from pass_generator import generate_password
import random
import string
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.minsize(width=400, height=300)
canvas = Canvas(width=200, height=224, highlightthickness=0)
logo = PhotoImage(file="day29/logo.png")
canvas.create_image(100, 112, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

site=Label(text="Website:")
site.grid(column=0, row=1)
site_entr=Entry(width=21)
site_entr.grid(column=1, row=1)
site_entr.focus()  # Set focus on the site entry field
search_button = Button(text="Search", width=14, command=lambda: search_password())
search_button.grid(column=2, row=1)

email=Label(text="Email/Username:")
email.grid(column=0, row=2)
email_entr=Entry(width=35)
email_entr.grid(column=1, row=2, columnspan=2)
email_entr.insert(0, "samuellywang@gmail.com")

password=Label(text="Password:")
password.grid(column=0, row=3)
pass_entr=Entry(width=21)
pass_entr.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=lambda: make_password())
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=lambda: save_password())
add_button.grid(column=1, row=4, columnspan=2)

def search_password():
    site = site_entr.get()
    try:
        with open("day29/passwords.json", "r") as file:
            data = json.load(file)
            if site in data:
                email = data[site]["email"]
                password = data[site]["password"]
                messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No password saved for {site}.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Seems you haven't saved any passwords yet. Do that first!")

def make_password():
    # Generate a random password with 12 characters, 2 uppercase, 2 lowercase, 2 numbers, and 2 symbols
    password = generate_password()
    pyperclip.copy(password)  # Copy the generated password to clipboard
    pass_entr.delete(0, END)  # Clear the entry field
    pass_entr.insert(0, password)

def save_password():
    site = site_entr.get()
    email = email_entr.get()
    password = pass_entr.get()
    new_data={
        site: {
            "email": email,
            "password": password
        }
    }
    if site and email and password:
        ok=messagebox.askokcancel(title=site, message=f"Details to save:\nEmail: {email}\nPassword: {password}\n\nAre you sure?")
        if ok:
            try:
                with open("day29/passwords.json", "r") as file:
                    data=json.load(file)
                data.update(new_data)
            except FileNotFoundError:
                data = new_data
            with open("day29/passwords.json", "w") as file:
                json.dump(data, file, indent=4)
            site_entr.delete(0, END)
            #email not deleted, since I always use 1 email
            pass_entr.delete(0, END)
    else:
        messagebox.showinfo(title="Password Manager", message="Please fill in all fields.")

window.mainloop()