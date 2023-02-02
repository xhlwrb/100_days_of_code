from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

DEFAULT_EMAIL = "xhlwrb@hotmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_clicked():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_clicked():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input,
        }
    }

    if website_input != "" and password_input != "":
        messagebox.askokcancel(title=website_input, message=f"There are the details entered:\nEmail: {email_input}\n"
                                                            f"Password: {password_input}\nIs it ok to save?")
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, DEFAULT_EMAIL)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


# ------------------------- SEARCH PASSWORD ---------------------------- #


def search_clicked():
    website_input = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=website_input, message="No data file found")
    else:
        if website_input in data:
            email = data[website_input]["email"]
            password = data[website_input]["password"]
            messagebox.showinfo(title=website_input, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website_input, message="No details for the website exists")
    finally:
        website_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=29)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus()

email_entry = Entry(width=48)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_entry.insert(0, DEFAULT_EMAIL)

password_entry = Entry(width=29)
password_entry.grid(column=1, row=3, sticky=W)

# Button
generate_button = Button(text="Generate Password",width=17, command=generate_clicked)
generate_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=47, command=add_clicked)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

search_button = Button(text="Search", width=17, command=search_clicked)
search_button.grid(column=2, row=1)


window.mainloop()
