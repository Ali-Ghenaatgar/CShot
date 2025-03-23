from tkinter import *
from tkinter import messagebox

usernames = ["admin", "user", "root"]
passwords = ["123", "1234", "12345"]

root = Tk()
root.title("Login")
root.geometry("800x600+300+200")  
root.resizable(False, False)  # This code helps to disable windows from resizing

img = PhotoImage(file="kali3.png")
Label(root, image=img, bg = "white").place(x=0, y=0)

frame = Frame(root,width=350, height=500, bg="white")
frame.place(x=400, y=50)

heading = Label(frame, text="Login", font=("Arial", 20, "bold"), bg="white", fg="#57a1f8")
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
def login():
    username = user.get()
    password = passcode.get()
    for i in range(len(usernames)):
        if username == usernames[i] and password == passwords[i]:
            messagebox.showinfo("Login", "Login Successful")
        elif username == usernames[i] and password != passwords[i]:
            messagebox.showerror("Login", "Incorrect Password")
        elif username != usernames[i] and password == passwords[i]:
            messagebox.showerror("Login", "Incorrect Username")
        # elif username != usernames[i] and password != passwords[i]:
        #     messagebox.showerror("Login", "Incorrect Username and Password")


login = Button(frame, text="Login", font=("Microsoft yaHei UI Light", 15, "bold"), bg="#57a1f8", fg="white", border=0, width=20, command=login)
login.place(x=55, y=350)

new_user_button = Label(frame, text="Don't have an account?", font=("Microsoft yaHei UI Light", 9), bg="white", fg="black").place(x=55, y=400)
sign_up = Button (frame,width=6, text="Sign Up", fg="#57a1f8", bg="white", border=0, cursor ="hand2")
sign_up.place(x=195, y=400)

root.mainloop()  # Start the main event loop
 

# command=lambda: messagebox.showinfo("Login", "Login Successful")