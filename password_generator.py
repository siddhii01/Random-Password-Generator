from tkinter import *
import string
import random
import pyperclip

def generate():
    # Clear the previous password
    pwdField.delete(0, 'end')

    small_case = string.ascii_lowercase
    capital_case = string.ascii_uppercase
    num = string.digits
    sp_char = string.punctuation

    combine = small_case + capital_case + num + sp_char
    pwd_len = int(length_Box.get())

    if choice.get() == 1:
        password = ''.join(random.sample(small_case + capital_case, pwd_len))
    elif choice.get() == 2:
        password = ''.join(random.sample(small_case + capital_case + num, pwd_len))
    elif choice.get() == 3:
        password = ''.join(random.sample(small_case + capital_case + num + sp_char, pwd_len))

    # Insert the new password
    pwdField.insert(0, password)

def copy():
    ran_pwd = pwdField.get()
    pyperclip.copy(ran_pwd.replace(" ", ""))

def reset():
    pwdField.delete(0, 'end')
    choice.set(None)
    var = IntVar()
    var.set(8)
    length_Box.config(textvariable=var)

pwdgen = Tk()
choice = IntVar()
var = IntVar()

pwdLabel = Label(pwdgen, text="Random Password Generator")
pwdLabel.grid()
msgLabel = Label(pwdgen, text="Please Choose Strength of Password")
msgLabel.grid(pady=4)

weakpwd = Radiobutton(pwdgen, text="weak", value=1, variable=choice)
weakpwd.grid()

medpwd = Radiobutton(pwdgen, text="medium", value=2, variable=choice)
medpwd.grid()

strpwd = Radiobutton(pwdgen, text="strong", value=3, variable=choice)
strpwd.grid()

lenLabel = Label(pwdgen, text="Select Length of Password")
lenLabel.grid(pady=4)

length_Box = Spinbox(pwdgen, from_=8, to_=18, textvariable=var)
length_Box.grid()

genButton = Button(pwdgen, text="Generate", command=generate)
genButton.grid(pady=8)

pwdField = Entry(pwdgen, width=25)
pwdField.grid()

resetButton = Button(pwdgen, text="Reset", command=reset)
resetButton.grid()

copyButton = Button(pwdgen, text="Copy Password", command=copy)
copyButton.grid(pady=8)

pwdgen.mainloop()
