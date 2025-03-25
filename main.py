from tkinter import *
from tkinter import messagebox
import re
from sqlalchemy import Column, Integer, String, Sequence, create_engine , update
from sqlalchemy.orm import sessionmaker, declarative_base
import pygame
import random
import math

engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

players = []
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    email = Column(String(100))
    win = Column(Integer)
    lose = Column(Integer)
    total_score = Column(Integer)

    def add_score(self, points):
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
            players.append(username)
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
        
        def on_enter_e(e):
            if email.get() == "Email":
                email.delete(0, "end")

        def on_leave_e(e):
            if email.get() == "":
                email.insert(0, "Email")
        email.bind("<FocusIn>", on_enter_e)
        email.bind("<FocusOut>", on_leave_e)

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
                players.append(username)
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

class Player():
    def __init__(self, x, y, circles, last_shot, sound, score=0, bullets=10, shotgun_bullets=0):
        # Initialize player with position, bullets, score, and sounds
        self.x = x
        self.y = y
        self.last_shot = last_shot
        self.sound = sound
        self.score = score
        self.bullets = bullets
        self.circles = circles
        self.shotgun_bullets = shotgun_bullets

    def shoot(self):
        # Handle shooting mechanics
        if self.bullets > 0:
            self.bullets -= 1
            if self.shotgun_bullets > 0:
                self.shotgun_bullets -= 1
                pygame.mixer.music.load(self.sound[1])
                pygame.mixer.music.play()
                self.circles.append([(self.x, self.y),(self.x+10, self.y),(self.x-10, self.y),(self.x, self.y-10),(self.x, self.y+10),(self.x+8,self.y-7),(self.x+6,self.y+4),(self.x-3,self.y-8),(self.x-4,self.y+4),(self.x-2,self.y-2),(self.x+2,self.y-6),(self.x+6,self.y+7),(self.x-7,self.y-6),(self.x+5,self.y)])
            else:
                pygame.mixer.music.load(self.sound[0])
                pygame.mixer.music.play()
                self.circles.append((self.x, self.y))
                
            # Check hits on regular targets
            for target in [target1, target2, target3]:
                if self.shotgun_bullets > 0:
                    if target.x - 10 < self.x < target.x + 60 and target.y - 10 < self.y < target.y + 60:
                        pygame.mixer.music.load('vay-hossein.wav')
                        pygame.mixer.music.play()
                        self.score += distance(self.x, self.last_shot[0],self.y, self.last_shot[1])
                        target.x = random.randint(0, 750)
                        target.y = random.randint(0, 550)
                else:
                    if target.x < self.x < target.x + 50 and target.y < self.y < target.y + 50:
                        pygame.mixer.music.load('vay-hossein.wav')
                        pygame.mixer.music.play()
                        self.score += distance(self.x, self.last_shot[0],self.y, self.last_shot[1])
                        target.x = random.randint(0, 750)
                        target.y = random.randint(0, 550)
            if self.shotgun_bullets > 0:
                if special_target1.x - 10 < self.x < special_target1.x + 60 and special_target1.y - 10 < self.y < special_target1.y + 60:
                    self.shotgun_bullets += 3
                    self.bullets += 3
                    self.score += distance(self.x, self.last_shot[0],self.y, self.last_shot[1])
                    pygame.mixer.music.load('reload.mp3')
                    pygame.mixer.music.play()
                    special_target1.x = 1000
                    special_target1.y = 1000
                    special_target1.show = False
                if special_target2.x - 10 < self.x < special_target2.x + 60 and special_target2.y - 10 < self.y < special_target2.y + 60:
                    self.bullets += 10
                    self.score += distance(self.x, self.last_shot[0],self.y, self.last_shot[1])
                    pygame.mixer.music.load('reload.mp3')
                    pygame.mixer.music.play()
                    special_target2.x = 1000
                    special_target2.y = 1000
                    special_target2.show = False
                if special_target3.x - 10 < self.x < special_target3.x + 60 and special_target3.y - 10 < self.y < special_target3.y + 60:
                    self.score *= 2
                    pygame.mixer.music.load('2x.mp3')
                    pygame.mixer.music.play()
                    special_target3.x = 1000
                    special_target3.y = 1000
                    special_target3.show = False
            else:
                if special_target1.x < self.x < special_target1.x + 50 and special_target1.y < self.y < special_target1.y + 50:
                    self.shotgun_bullets += 3
                    self.bullets += 3
                    self.score += distance(self.x, self.last_shot[0],self.y, self.last_shot[1])
                    pygame.mixer.music.load('reload.mp3')
                    pygame.mixer.music.play()
                    special_target1.show = False
                if special_target2.x < self.x < special_target2.x + 50 and special_target2.y < self.y < special_target2.y + 50:
                    self.bullets += 10
                    self.score += distance(self.x, self.last_shot[0],self.y, self.last_shot[1])
                    special_target2.show = False
                if special_target3.x < self.x < special_target3.x + 50 and special_target3.y < self.y < special_target3.y + 50:
                    self.score *= 2
                    pygame.mixer.music.load('2x.mp3')
                    pygame.mixer.music.play()
                    special_target3.show = False
            self.last_shot[0] = self.x
            self.last_shot[1] = self.y

class Target():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def render(self, screen):
        # Draw target on screen
        screen.blit(self.image, (self.x, self.y))

class SpecialTarget(Target):
    def __init__(self, x, y, image, start_time, interval):
        # Special target with timing
        super().__init__(x, y, image)
        self.show = False
        self.start_time = start_time
        self.show_duration = 4000
        self.interval = interval  

    def update(self):
        # Control when special target appears
        current_time = pygame.time.get_ticks()
        
        if not self.show and current_time - self.start_time >= self.interval:
            self.show = True
            self.start_time = current_time  
            self.x = random.randint(0, 750)
            self.y = random.randint(0, 550)

        if self.show and current_time - self.start_time >= self.show_duration:
            self.show = False

    def render(self, screen):
        # Draw special target if visible
        if self.show:
            screen.blit(self.image, (self.x, self.y))

def distance(x1, x2, y1, y2):
    # Calculate distance for scoring
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    score_plus = int(distance/100)
    score_plus += 1
    return score_plus

# Setup game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('CShot')
icon = pygame.image.load("shooting-range.png")
pygame.display.set_icon(icon)

# Load images and sounds
target_image = pygame.image.load('target.png')
target_image = pygame.transform.scale(target_image, (50, 50))
shotgun_bullet_image = pygame.image.load('shotgun_bullets.png')
shotgun_bullet_image = pygame.transform.scale(shotgun_bullet_image, (50, 50))
extra_ammo_image = pygame.image.load('extra_ammo.png')
extra_ammo_image = pygame.transform.scale(extra_ammo_image, (50, 50))
double_points_image = pygame.image.load('double-points.png')
double_points_image = pygame.transform.scale(double_points_image, (50, 50))
sound1 = ['bullet1.wav','shotgun1.wav']
sound2 = ['bullet2.wav',('shotgun2.wav')]

# Create players and targets
player1 = Player(random.randint(0, 775), random.randint(0, 575), circles=[], last_shot=[0,0], sound=sound1)
player2 = Player(random.randint(0, 775), random.randint(0, 575), circles=[], last_shot=[0,0], sound=sound2)
 

def player(player):
    # Draw player
    screen.blit(screen, (player.x, player.y))

target1 = Target(random.randint(0, 750), random.randint(0, 550), target_image)
target2 = Target(random.randint(0, 750), random.randint(0, 550), target_image)
target3 = Target(random.randint(0, 750), random.randint(0, 550), target_image)

special_target1 = SpecialTarget(random.randint(0, 750), random.randint(0, 550), shotgun_bullet_image, start_time=0, interval=5000)
special_target2 = SpecialTarget(random.randint(0, 750), random.randint(0, 550), extra_ammo_image, start_time=0, interval=7000)
special_target3 = SpecialTarget(random.randint(0, 750), random.randint(0, 550), double_points_image, start_time=0, interval=13000)

# Movement variables
xchange1, ychange1 = 0, 0
xchange2, ychange2 = 0, 0

pygame.init()
font = pygame.font.Font(None, 20)
start_time = pygame.time.get_ticks()
game_duration = 10000


# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))
    player(player1)
    player(player2)
    # Calculate remaining time
    elapsed_time = pygame.time.get_ticks() - start_time
    remaining_time = max(0, (game_duration - elapsed_time) // 1000)
    if remaining_time == 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Player 1 movement
            if event.key == pygame.K_w:
                ychange1 = -0.2
            if event.key == pygame.K_s:
                ychange1 = 0.2
            if event.key == pygame.K_a:
                xchange1 = -0.2
            if event.key == pygame.K_d:
                xchange1 = 0.2
            # Player 2 movement
            if event.key == pygame.K_UP:
                ychange2 = -0.2
            if event.key == pygame.K_DOWN:
                ychange2 = 0.2
            if event.key == pygame.K_LEFT:
                xchange2 = -0.2
            if event.key == pygame.K_RIGHT:
                xchange2 = 0.2
            # Shooting controls
            if event.key == pygame.K_TAB:
                player1.shoot()
            if event.key == pygame.K_RETURN:
                player2.shoot()

        if event.type == pygame.KEYUP:
            # Stop movement
            if event.key in [pygame.K_a, pygame.K_d]:
                xchange1 = 0
            if event.key in [pygame.K_w, pygame.K_s]:
                ychange1 = 0
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                xchange2 = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                ychange2 = 0
        
    # Update player positions
    player1.x , player1.y = max(0, min(player1.x + xchange1, 775)) , max(0, min(player1.y + ychange1, 575))
    player2.x , player2.y = max(0, min(player2.x + xchange2, 775)) , max(0, min(player2.y + ychange2, 575))

    # Draw targets and bullets
    for target_obj in [target1, target2, target3, special_target1, special_target2, special_target3]:
        target_obj.render(screen)

    for circle in player1.circles:
        # Draw player 1's bullets
        if type(circle) == tuple:
            pygame.draw.circle(screen, (255, 0, 0), circle, 2)
        else:
            for i in circle:
                pygame.draw.circle(screen, (255, 0, 0), i, 3)
    for circle in player2.circles:
        # Draw player 2's bullets
        if type(circle) == tuple:
            pygame.draw.circle(screen, (0, 0, 255), circle, 2)
        else:
            for j in circle:
                pygame.draw.circle(screen, (0, 0, 255), j, 3)

    # Display scores and info
    
    score_text1 = font.render(f"{players[0]} : {player1.score}", True, (0, 0, 0))
    score_text2 = font.render(f"{players[1]} : {player2.score}", True, (0, 0, 0))
    remaining_bullets1 = font.render(f"{players[0]}'s Bullets: {player1.bullets}", True, (0, 0, 0)) if player1.bullets > 0 else font.render(f"Player 1 Bullets: {player1.bullets}", True, (255, 0, 0))
    remaining_bullets2 = font.render(f"{players[1]}'s Bullets: {player2.bullets}", True, (0, 0, 0)) if player2.bullets > 0 else font.render(f"Player 2 Bullets: {player2.bullets}", True, (255, 0, 0))
    time_left = font.render(f"Time Left: {remaining_time}s", True, (0, 0, 0))

    screen.blit(score_text1, (10, 10))
    screen.blit(score_text2, (10, 30))
    screen.blit(remaining_bullets1, (10, 50))
    screen.blit(remaining_bullets2, (10, 70))
    screen.blit(time_left, (10, 90))

    pygame.display.update()  # Update screen
    
    # Update special targets
    for special_target in [special_target1, special_target2, special_target3]:
        special_target.update()

pygame.quit()  # Exit game

game_over = Tk()
game_over.title("Game Over")
game_over.geometry("800x600+300+50")
game_over.resizable(False, False)
background = PhotoImage(file="kali3.png")
Label(game_over, image=background, bg = "white").place(x=-2, y=0)
frame = Frame(game_over,width=350, height=500, bg="white")
frame.place(x=400, y=50)
    
if player1.score > player2.score:
    winner = Label(frame, text=f"{players[0]} Wins!", font=("Arial", 25, "bold"), bg="white", fg="red")
    winner.place(x=60, y=150)
    session.execute(update(User).where(User.username == players[0]).values(win=User.win + 1))
    session.execute(update(User).where(User.username == players[1]).values(lose=User.lose + 1))
    session.execute(update(User).where(User.username == players[0]).values(total_score=User.total_score + player1.score))
    session.execute(update(User).where(User.username == players[1]).values(total_score=User.total_score + player2.score))
    session.commit()

elif player1.score < player2.score:
    winner = Label(frame, text=f"{players[1]} Wins!", font=("Arial", 25, "bold"), bg="white", fg="blue")
    winner.place(x=60, y=150)
    session.execute(update(User).where(User.username == players[1]).values(win=User.win + 1))
    session.execute(update(User).where(User.username == players[0]).values(lose=User.lose + 1))
    session.execute(update(User).where(User.username == players[0]).values(total_score=User.total_score + player1.score))
    session.execute(update(User).where(User.username == players[1]).values(total_score=User.total_score + player2.score))
    session.commit()
else:
    winner = Label(frame, text="It's a tie!", font=("Arial", 25, "bold"), bg="white", fg="gray")
    winner.place(x=105, y=150)
    session.execute(update(User).where(User.username == players[0]).values(total_score=User.total_score + player1.score))
    session.execute(update(User).where(User.username == players[1]).values(total_score=User.total_score + player2.score))

top_users = session.query(User.username).order_by(User.win.desc()).limit(3).all()
top_usernames = [username[0] for username in top_users]



heading = Label(frame, text="Game Over", font=("Arial", 30, "bold"), bg="white", fg="black")
heading.place(x=70, y=35)
score1 = Label(frame, text=f"{players[0]}'s Score: {player1.score}", font=("Arial", 20, "bold"), bg="white", fg="red")
score1.place(x=60, y=200)
score2 = Label(frame, text=f"{players[1]}'s Score: {player2.score}", font=("Arial", 20, "bold"), bg="white", fg="blue")
score2.place(x=60, y=250)
def show_leaderboard():

    leaderboard = Toplevel(game_over)
    leaderboard.title("Leaderboard")
    leaderboard.geometry("800x600+300+50")
    leaderboard.resizable(False, False)
    background = PhotoImage(file="kali3.png")
    Label(leaderboard, image=background, bg = "white").place(x=-2, y=0)
    frame = Frame(leaderboard,width=350, height=500, bg="white")
    frame.place(x=400, y=50)
    heading = Label(frame, text="Leaderboard", font=("Arial", 30, "bold"), bg="white", fg="black")
    heading.place(x=70, y=35)
    first_wins = session.query(User.win).filter(User.username == top_usernames[0]).first()
    
    first = Label(frame, text=f"1. {top_usernames[0]}: {first_wins} wins", font=("Arial", 15, "bold"), bg="white", fg="#ffd700")
    first.place(x=60, y=150)
    second_wins = session.query(User.win).filter(User.username == top_usernames[1]).first()

    second = Label(frame, text=f"2. {top_usernames[1]}: {second_wins} wins", font=("Arial", 15, "bold"), bg="white", fg="#c0c0c0")
    second.place(x=60, y=200)
    third_wins = session.query(User.win).filter(User.username == top_usernames[2]).first()

    third = Label(frame, text=f"3. {top_usernames[2]}: {third_wins} wins", font=("Arial", 15, "bold"), bg="white", fg="#cd7f32")
    third.place(x=60, y=250)
    leaderboard.mainloop()

leader_board = Button(frame, text="Leaderboard", font=("Arial", 20, "bold"), bg="black", fg="white", cursor="hand2", command = show_leaderboard)
leader_board.place(x=80, y=350)
game_over.mainloop()