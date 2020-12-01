from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password} \n")
            website_input.delete(0, END)
            password_input.delete(0, END)

    if len(website) == 0 or len(password) == 0:
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=2)

website_label = Label(text="Website:", font=("Arial", 16, "normal"))
website_label.grid(row=2, column=1)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=2, column=2, columnspan=2)

email_label = Label(text="Email/Username:", font=("Arial", 16, "normal"))
email_label.grid(row=3, column=1)

email_input = Entry(width=35)
email_input.grid(row=3, column=2, columnspan=2)
email_input.insert(0, "example@example.com")

password_label = Label(text="Password:", font=("Arial", 16, "normal"))
password_label.grid(row=4, column=1)

password_input = Entry(width=21)
password_input.grid(row=4, column=2)

password_button = Button(text="Generate Password")
password_button.grid(row=4, column=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=2, columnspan=2)


window.mainloop()