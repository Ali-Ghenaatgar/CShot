from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")  
root.resizable(False, False)  # This code helps to disable windows from resizing

img = PhotoImage(file="kali2.png")
Label(root, image=img, bg = "white").place(x=0, y=0)

frame = Frame(root,width=350, height=400, bg="white")
frame.place(x=500, y=50)

heading = Label(frame, text="Login", font=("Arial", 20, "bold"), bg="white", fg="#57a1f8")
heading.place(x=140, y=15)

username = Entry(frame, font=("Microsoft yaHei UI Light", 15), bg="white", fg="black", border=0, width=20)
username.place(x=30, y=100)
username.insert(0, "Username")
Frame(frame, width=250, height=2, bg="black").place(x=30, y=130)

password = Entry(frame, font=("Microsoft yaHei UI Light", 15), bg="white", fg="black", border=0, width=20)
password.place(x=30, y=170)
password.insert(0, "Password")  
Frame(frame, width=250, height=2, bg="black").place(x=30, y=200)


root.mainloop()  # Start the main event loop
