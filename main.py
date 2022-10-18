"""A password generator using tkinter."""

import tkinter
from tkinter import messagebox
import char_list
import random
import pyperclip
import json


# Functions
def save_password():
    """Writes the user password to data.json file."""

    # Creates a new dictionary with the user inputs.
    new_data = {
        website.get(): {
            "email": email.get(),
            "password": password.get()
        }
    }

    # If/else requiring the user to fill all text fields.
    if website.get() and email.get() and password.get():

        # Confirmation message.
        messagebox.showinfo(title="MyPass | Password Manager", message="Confirmed: Your information was saved.",
                            icon="info")

        try:
            with open("data.json", "r") as data_file:
                # Loads (reads) the existing data.
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Dumps (writes) the new_data to the data.json file.
                json.dump(new_data, data_file, indent=4)
        else:
            # Updates the existing data with the new_data.
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Dumps (writes) the new_data to the data.json file.
                json.dump(data, data_file, indent=4)
        finally:
            # Deletes the user info from the entries.
            website_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")

    else:

        # Error message if any fields are missing info.
        messagebox.showerror(title="MyPass | Password Manager", message="Error: All fields are required", icon="error")


def generate_password():
    """Generates a random password using letters, numbers, and symbols."""

    # Generates random numbers.
    num_random_letters = random.randint(8, 10)
    num_random_numbers = random.randint(2, 4)
    num_random_symbols = random.randint(2, 4)

    # Empty list.
    password_list = []

    # Loops through the letters, numbers, and symbols from char_list and appends it to our password_list.
    for char in range(num_random_letters):
        password_list.append(char_list.letters[char])
    for char in range(num_random_numbers):
        password_list.append(char_list.numbers[char])
    for char in range(num_random_symbols):
        password_list.append(char_list.symbols[char])

    # Shuffles our password_list.
    random.shuffle(password_list)

    # Joins the password_list and stores it in random_password.
    random_password = "".join(password_list)

    # Inserts the password into the password entry
    password_entry.insert(0, random_password)

    # Copies the password to the clipboard
    pyperclip.copy(random_password)


# Creates our window instance and sets title.
window = tkinter.Tk()
window.title("MyPass | Password Manager")
window.config(padx=50, pady=50)

# Creates our logo.
canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Creates our icon.
icon = tkinter.PhotoImage(file="logo.png")
window.iconphoto(False, icon)

# Labels.
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

# Focuses the cursor in the website Entry.
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

# Keeps program window open.
window.mainloop()
