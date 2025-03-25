from tkinter import *
from tkinter import messagebox

usernames = ["admin", "user", "root"]
passwords = ["123", "1234", "12345"]

window = Tk()
window.title("Sign Up")
window.geometry("800x600+300+50")  
window.resizable(False, False)  # This code helps to disable windows from resizing

img = PhotoImage(file="kali3.png")
Label(window, image=img, bg = "white").place(x=-2, y=0)

frame = Frame(window,width=350, height=500, bg="white")
frame.place(x=400, y=50)

heading = Label(frame, text="Sign up", font=("Arial", 20, "bold"), bg="white", fg="#57a1f8")
heading.place(x=140, y=15)

user = Entry(frame, font=("Microsoft yaHei UI Light", 15), bg="white", fg="black", border=0, width=20)
user.place(x=30, y=100)
user.insert(0, "Username")
def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    if user.get() == "":
        user.insert(0, "Username")  

user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=270, height=2, bg="black").place(x=30, y=130)

passcode = Entry(frame, font=("Microsoft yaHei UI Light", 15), bg="white", fg="black", border=0, width=20)
passcode.place(x=30, y=170)
passcode.insert(0, "Password")  
Frame(frame, width=270, height=2, bg="black").place(x=30, y=200)
def on_enter(e):
    passcode.delete(0, "end")

def on_leave(e):
    if passcode.get() == "":
        passcode.insert(0, "password")  
        
passcode.bind("<FocusIn>", on_enter)
passcode.bind("<FocusOut>", on_leave)
#--------------------------------------------------------------------------------
def signup():
    username = user.get()
    password = passcode.get()
    if username not in usernames:
        messagebox.showinfo("Sign up", "Sign up Successful")
        # user.delete(0, "end")
        # passcode.delete(0, "end")
        user.insert(0, "Username")
        passcode.insert(0, "Password")
    else:
        messagebox.showerror("Sign up", "Username already exists.")


sign_up = Button(frame, text="Sign up", font=("Microsoft yaHei UI Light", 15, "bold"), bg="#57a1f8", fg="white", border=0, width=20, command=signup)
sign_up.place(x=55, y=350)
# def sign_up():
#     username = user.get()
#     password = passcode.get()
#     if username in usernames:
#         messagebox.showerror("Sign Up", "Username already exists")
#     else:
#         usernames.append(username)
#         passwords.append(password)
#         messagebox.showinfo("Sign Up", "Sign Up Successful")
#         user.delete(0, "end")
#         passcode.delete(0, "end")
#         user.insert(0, "Username")
#         passcode.insert(0, "Password")
            

new_user_button = Label(frame, text="Have an account?", font=("Microsoft yaHei UI Light", 9), bg="white", fg="black").place(x=55, y=400)
sign_in = Button (frame,width=6, text="Sign in", fg="#57a1f8", bg="white", border=0, cursor ="hand2")
sign_in.place(x=195, y=400)


window.mainloop()  # Start the main event loop