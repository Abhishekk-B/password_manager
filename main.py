from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(choice(letters))

    for char in range(nr_symbols):
        password_list += choice(symbols)

    for char in range(nr_numbers):
        password_list += choice(numbers)

    shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    print(f"Your password is: {password}")

    password_box.delete(0, END)
    password_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_box.get()
    email_data = username_box.get()
    password_data = password_box.get()

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="warning", message= "The fields are empty")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered:\nEmail : {email_data}\n"
                                                       f"password : {password_data}\n is it okay?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_data} | {email_data} | {password_data}\n")
                website_box.delete(0, END)
                password_box.delete(0, END)
                website_box.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
# window.minsize(width=400, height=400)
window.config(padx=20, pady=20, bg="white")
logo = PhotoImage(file="logo.png")

canva = Canvas()
canva.config(width=200, height=200, bg = 'white', highlightthickness=0)
canva.create_image(100,100,image= logo)
canva.grid(row=1, column=2)

website = Label(text="Website", bg="white")
website.grid(row = 2, column= 1)

username = Label(text="Username/Email", bg="white")
username.grid(row = 3, column= 1)

password_1 = Label(text="Password", bg="white")
password_1.grid(row = 4, column= 1)

website_box = Entry(width=43)
website_box.grid(row=2, column=2, columnspan=2)
website_box.focus()

username_box = Entry(width=43)
username_box.grid(row=3, column=2, columnspan=2)
username_box.insert(0,"ABC@xyz.com")

password_box = Entry(width=25)
password_box.grid(row=4, column=2)

generate_password = Button(text="Generate Password", command=generator)
generate_password.grid(row=4, column=3)
#
add = Button(text="Add",  width=34, command=save)
add.grid(row=5, column=2, columnspan=2)

window.mainloop()
