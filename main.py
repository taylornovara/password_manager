"""A password generator using tkinter."""
import tkinter

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
website_entry = tkinter.Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password", width=11)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=35)
add_button.grid(row=4, column=1, columnspan=2)

# Keeps program window open
window.mainloop()
