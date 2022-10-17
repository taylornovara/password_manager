"""A password generator using tkinter."""
import tkinter
import char_list
import random


# Functions
def save_password():
    with open("data.txt", "a") as data:
        data.write(f"{website.get()} | {email.get()} | {password.get()} \n")
        website_entry.delete(0, "end")
        email_entry.delete(0, "end")
        password_entry.delete(0, "end")


def generate_password():
    pass


# Creates our window instance and sets title
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creates our logo
canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

# Creates a string instance, so we can store the user input.
website = tkinter.StringVar()

# User input is saved into the text variable as a string.
website_entry = tkinter.Entry(width=37, textvariable=website)
website_entry.grid(row=1, column=1, columnspan=2)

# Focuses the cursor in the website Entry
website_entry.focus()

# Creates a string instance, so we can store the user input.
email = tkinter.StringVar()

# User input is saved into the text variable as a string.
email_entry = tkinter.Entry(width=37, textvariable=email)
email_entry.grid(row=2, column=1, columnspan=2)

# Creates a string instance, so we can store the user input.
password = tkinter.StringVar()

# User input is saved into the text variable as a string.
password_entry = tkinter.Entry(width=21, textvariable=password, show="*")
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

# Keeps program window open
window.mainloop()
