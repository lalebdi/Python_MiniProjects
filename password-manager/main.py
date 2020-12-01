from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=2)

website_label = Label(text="Website:", font=("Arial", 16, "normal"))
website_label.grid(row=2, column=1)

website_input = Entry(width=35)
website_input.grid(row=2, column=2, columnspan=2)

email_label = Label(text="Email/Username:", font=("Arial", 16, "normal"))
email_label.grid(row=3, column=1)

email_input = Entry(width=35)
email_input.grid(row=3, column=2, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 16, "normal"))
password_label.grid(row=4, column=1)

password_input = Entry(width=21)
password_input.grid(row=4, column=2)

password_button = Button(text="Generate Password")
password_button.grid(row=4, column=3)

add_button = Button(text="Add", width=36)
add_button.grid(row=5, column=2, columnspan=2)


window.mainloop()