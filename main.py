"""A password generator using tkinter."""
import tkinter

# Creates our window instance and sets title
window = tkinter.Tk()
window.title("Locked | Password Manager")
window.config(pady=20, padx=20, bg="red")

# Setting window size
window_width = 600
window_height = 400

# Get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Set the position of the window to the center of the screen, prevents user from changing window size
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)

# Creates logo
canvas = tkinter.Canvas(window, bg="white", highlightthickness=0)
canvas.place(relx=0.5, rely=0.5, anchor="center")
logo = tkinter.PhotoImage(file="locked.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = tkinter.Label(text="Website:", bg="white", fg='black')
website_label.grid(row=1, column=0)

username_label = tkinter.Label(text="Username:", bg="white", fg='black')
username_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:", bg="white", fg='black')
password_label.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=35, bg="white", highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2)

username_entry = tkinter.Entry(width=35, bg="white", highlightthickness=0)
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = tkinter.Entry(width=35, bg="white", highlightthickness=0)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password", width=10, bg="white", highlightthickness=0)
generate_password_button.grid(row=4, column=2)

add_button = tkinter.Button(text="Add", width=10, bg="white", highlightthickness=0)
add_button.grid(row=4, column=1)

# Keeps program window open
window.mainloop()
