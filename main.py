import tkinter
from tkinter import *
from tkinter import messagebox

FONT_NAME = 'Calibri'
FONT_SIZE = 12

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# Padlock image
canvas = Canvas(width=200, height=210)
padlock = PhotoImage(file='lock.gif')
canvas.create_image(100, 103, image=padlock)


def view_saved_details():
    top = tkinter.Toplevel()
    top.title("Account Details")
    with open('data.txt', 'r') as f:
        data = f.read()
    data_label = Label(top, text=data)
    data_label.pack()


def ok_or_cancel():
    """Display message box and ask user to press OK or CANCEL."""
    ok_cancel = messagebox.askokcancel(title="Are you sure?",
                message="Press OK to confirm, press CANCEL to cancel.")
    if ok_cancel:
        return True
    return False


def empty_field_error():
    """Display message box telling user not to leave any fields empty."""
    if len(website_entry.get().strip()) == 0 or len(password_entry.get().
                                                    strip()) == 0:
        messagebox.showerror(title="Empty Fields",
                             message="Please don't leave the website or "
                                     "password fields empty!")
        return False
    return True


def delete_and_focus():
    """Deletes data from website and password entry fields and sets input
    focus onto the website entry widget."""
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    website_entry.focus()


def add_info():
    """
    Take in all entry field data and store them into 'data.txt'.
    Delete site and password entry fields and set focus onto the site
     field.
    """
    site = website_entry.get()
    email = email_entry.get()
    user = username_entry.get()
    pw = password_entry.get()

    empty_field = empty_field_error()
    if empty_field:

        confirm = ok_or_cancel()
        if confirm:
            with open('data.txt', 'a') as f_obj:
                f_obj.write(f"{site} | {email} | {user} | {pw}\n")

            delete_and_focus()


# Labels
website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE, 'normal'),
                      borderwidth=0, highlightthickness=0)

email_label = Label(text="Email:", font=(FONT_NAME, FONT_SIZE,
                                                  'normal'))

username_label = Label(text="Username:", font=(FONT_NAME, FONT_SIZE, 'normal'))

password_label = Label(text='Password:', font=(FONT_NAME, FONT_SIZE, 'normal'))


# Entries
website_entry = Entry(width=40)
website_entry.focus()
email_entry = Entry(width=40)
username_entry = Entry(width=40)
password_entry = Entry(width=40)

# Buttons
generate_button = Button(text="View Account Details", command=view_saved_details)
add_button = Button(text="Add", width=36, command=add_info)


# Widget layout
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
username_label.grid(row=3, column=0)
password_label.grid(row=4, column=0)

website_entry.grid(row=1, column=1, columnspan=1)
email_entry.grid(row=2, column=1, columnspan=1)
username_entry.grid(row=3, column=1)
password_entry.grid(row=4, column=1)

generate_button.grid(row=4, column=2)
add_button.grid(row=5, column=1, columnspan=1, pady=5)


window.mainloop()
