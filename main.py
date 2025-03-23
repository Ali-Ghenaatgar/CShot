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
root.mainloop()  # Start the main event loop
