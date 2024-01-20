from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
FONT = ("Arial", 16, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    clear_text(password_input)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_text(entry):
    entry.delete(0, "end")

def save_info():
    website_info = website_input.get()
    email_info = email_input.get()
    password_info = password_input.get()
    newj_data = {
        website_info: {
            "email": email_info,
            "password": password_info,
        }
    }
    if len(website_info) == 0  or len(email_info) == 0 or len(password_info) == 0:
        messagebox.showerror(message="Don't leave any of the fields empty")

    else:
        is_ok = messagebox.askokcancel(title= website_info, message=f"These are the details entered: \nEmail: "
                                                                f"{email_info}\nPassword: {password_info}\n"
                                                                f" Do you want to save?")
        if is_ok:
            try:
                with open("information.json", "r") as dataj_info:
                    data = json.load(dataj_info)
            except FileNotFoundError:
                with open("information.json", "w") as dataj_info:
                    json.dump(newj_data, dataj_info, indent= 4)
            else:
                data.update(newj_data)
                with open("information.json", "w") as dataj_info:
                    json.dump(data, dataj_info, indent=4)
            finally:
                clear_text(website_input)
                clear_text(email_input)
                clear_text(password_input)

def find_password():
    website_info = website_input.get()
    try:
        with open("information.json", "r") as dataj_info:
            data = json.load(dataj_info)
    except FileNotFoundError:
        messagebox.showerror(title="error", message="No data file found")
    else:
        if website_info in data:
            email = data[website_info]["email"]
            password = data[website_info]["password"]
            messagebox.showinfo(title= website_info, message=f"Website: {website_info}\n Email: {email}\n Password:"
                                                             f" {password}")
        else:
            messagebox.showerror(title= "error", message="No website found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=FONT)
website.grid(column=0, row=1)
website_input= Entry(width=21)
website_input.focus()
website_input.grid(column= 1, row=1)

email_username = Label(text="Email/Username:", font=FONT)
email_username.grid(column=0, row=2)
email_input = Entry(width=37)
email_input.grid(column=1, row=2, columnspan= 2)

password = Label(text="Password:", font= FONT)
password.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate password", width=12, command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=12, command= find_password)
search_button.grid(column= 2,row =1)

add_button = Button(text="Add", width=34, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()


