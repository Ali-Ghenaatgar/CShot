from tkinter import *
from tkinter import messagebox
import re
from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    email = Column(String(100))
    win = Column(Integer)
    lose = Column(Integer)
    total_score = Column(Integer)

    def add_score(self, points=20):
        user = session.query(User).filter_by(username=self.username).first()
        if user:
            user.total_score += points
            session.commit()

Base.metadata.create_all(engine)

def add_user_if_not_exists(username, password, email, win, lose, total_score):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user is None:
        new_user = User(username=username, password=password, email=email, win=win, lose=lose, total_score=total_score)
        session.add(new_user)
        session.commit()
        messagebox.showinfo("Sign up", "Sign up Successful")
        root.destroy()
    else:
        messagebox.showerror("Sign up", "User already exists")

def login_user(username, password):
    user = session.query(User).filter_by(username=username).first()
    if user:
        if user.password == password:
            messagebox.showinfo("Login", "Login Successful")
            return True
        else:
            messagebox.showerror("Login", "Incorrect Password")
            return False
    else:
        messagebox.showerror("Login", "User  not found")
        return False
#----------------------------------------------------------------

for i in range (2):
    root = Tk()
    root.title("Login")
    root.geometry("800x600+300+50")  
    root.resizable(False, False)

    img = PhotoImage(file="kali3.png")
    Label(root, image=img, bg = "white").place(x=-2, y=0)

    frame = Frame(root,width=350, height=500, bg="white")
    frame.place(x=400, y=50)

    heading = Label(frame, text="Login", font=("Arial", 20, "bold"), bg="white", fg="#57a1f8")
    heading.place(x=140, y=15)

    user = Entry(frame, font=("Microsoft yaHei UI Light", 15), bg="white", fg="black", border=0, width=20)
    user.place(x=30, y=100)
    user.insert(0, "Username")
    def on_enter(e):
        if user.get()== "Username":
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
        if passcode.get() == "Password":
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
        if login_user(username, password):
            root.destroy()


    login = Button(frame, text="Login", font=("Microsoft yaHei UI Light", 15, "bold"), bg="#57a1f8", fg="white", border=0, width=20, command=login)
    login.place(x=55, y=350)

    def login_command():
        window.destroy()

    def signup_command():
        global window

        window = Toplevel(root)
        window.title("Sign Up")
        window.geometry("800x600+300+50")  
        window.resizable(False, False)

        img = PhotoImage(file="kali3.png")
        Label(window, image=img, bg = "white").place(x=-2, y=0)

        frame = Frame(window,width=350, height=500, bg="white")
        frame.place(x=400, y=50)

        heading = Label(frame, text="Sign up", font=("Arial", 20, "bold"), bg="white", fg="#57a1f8")
        heading.place(x=120, y=15)

        user = Entry(frame, font=("Microsoft yaHei UI Light", 15), bg="white", fg="black", border=0, width=20)
        user.place(x=30, y=100)
        user.insert(0, "Username")
        def on_enter(e):
            if user.get() == "Username":
                user.delete(0, "end")

        def on_leave(e):
            if user.get() == "":
                user.insert(0, "Username")  

        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        Frame(frame, width=270, height=2, bg="black").place(x=30, y=130)

        passcode = Entry(frame, font=("Microsoft yaHei UI Light", 15), bg="white", fg="black", border=0, width=20)
        passcode.place(x=30, y=155)
        passcode.insert(0, "Password")  
        Frame(frame, width=270, height=2, bg="black").place(x=30, y=185)

        # confirm_passcode = Entry(frame, font=("Microsoft yaHei UI Light", 15), bg="white", fg="black", border=0, width=20)
        # confirm_passcode.place(x=30, y=210)
        # confirm_passcode.insert(0, "Confirm Password")
        # Frame(frame, width=270, height=2, bg="black").place(x=30, y=240)

        email = Entry(frame, font=("Microsoft yaHei UI Light", 15), bg="white", fg="black", border=0, width=20)
        email.place(x=30, y=265)
        email.insert(0, "Email")
        Frame(frame, width=270, height=2, bg="black").place(x=30, y=295)

        # if passcode.get() != confirm_passcode.get() or (passcode.get() != "Password" or confirm_passcode.get() != "Confirm Password"):
        #     messagebox.showerror("Sign up", "Passwords do not match")
        def validate_email(email):
            regex = r'[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}'
            if re.match(regex, email):
                return True
            return False
        
        def on_enter(e):
            if user.get() == "Email":
                user.delete(0, "end")

        def on_leave(e):
            if user.get() == "":
                user.insert(0, "Email")
        def on_enter(e):
            if passcode.get() == "Password" :
                passcode.delete(0, "end")

        def on_leave(e):
            if passcode.get() == "":
                passcode.insert(0, "Password")  
                
        passcode.bind("<FocusIn>", on_enter)
        passcode.bind("<FocusOut>", on_leave)
    
        def signup():
            global username,password
            username = user.get()
            password = passcode.get()
            
            if validate_email(email.get()) and (username != "Username" or username != "") and (password != "Password" or password != ""):
                add_user_if_not_exists(username,password,email.get(),win=0,lose=0,total_score=0)
            else:  
                if username == "Username":
                    messagebox.showerror("Sign up", "Enter your username")
                elif password == "Password":
                    messagebox.showerror("Sign up", "Enter your password")
                elif not validate_email(email.get()):
                    messagebox.showerror("Sign up", "Enter a valid email address")


        sign_up = Button(frame, text="Sign up", font=("Microsoft yaHei UI Light", 15, "bold"), bg="#57a1f8", fg="white", border=0, width=20, command=signup)
        sign_up.place(x=55, y=350)
                    
        new_user_button = Label(frame, text="Have an account?", font=("Microsoft yaHei UI Light", 9), bg="white", fg="black").place(x=55, y=400)
        sign_in = Button (frame,width=6, text="Log in", fg="#57a1f8", bg="white", border=0, cursor ="hand2",command=login_command)
        sign_in.place(x=165, y=400)

        window.transient(root)  # Make the sign-up window transient to the root window
        window.grab_set()  # Grab all the events for the sign-up window
        window.mainloop()  # Start the main event loop

    #--------------------------------------------------------------------------------

                
    new_user_button = Label(frame, text="Don't have account?", font=("Microsoft yaHei UI Light", 9), bg="white", fg="black").place(x=55, y=400)
    sign_up = Button (frame,width=6, text="Sign up", fg="#57a1f8", bg="white", border=0, cursor ="hand2",command = signup_command)
    sign_up.place(x=185, y=400)


    root.mainloop()