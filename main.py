import pygame
import random
import math
from tkinter import *
from tkinter import messagebox

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
    score_text1 = font.render(f"Player 1: {player1.score}", True, (0, 0, 0))
    score_text2 = font.render(f"Player 2: {player2.score}", True, (0, 0, 0))
    remaining_bullets1 = font.render(f"Player 1 Bullets: {player1.bullets}", True, (0, 0, 0)) if player1.bullets > 0 else font.render(f"Player 1 Bullets: {player1.bullets}", True, (255, 0, 0))
    remaining_bullets2 = font.render(f"Player 2 Bullets: {player2.bullets}", True, (0, 0, 0)) if player2.bullets > 0 else font.render(f"Player 2 Bullets: {player2.bullets}", True, (255, 0, 0))
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
heading = Label(frame, text="Game Over", font=("Arial", 30, "bold"), bg="white", fg="black")
heading.place(x=70, y=45)
score1 = Label(frame, text=f"Player 1 Score: {player1.score}", font=("Arial", 20, "bold"), bg="white", fg="red")
score1.place(x=60, y=300)
score2 = Label(frame, text=f"Player 2 Score: {player2.score}", font=("Arial", 20, "bold"), bg="white", fg="blue")
score2.place(x=60, y=350)
if player1.score > player2.score:
    winner = Label(frame, text="Player 1 Wins!", font=("Arial", 25, "bold"), bg="white", fg="red")
    winner.place(x=60, y=150)
elif player1.score < player2.score:
    winner = Label(frame, text="Player 2 Wins!", font=("Arial", 25, "bold"), bg="white", fg="blue")
    winner.place(x=60, y=150)
else:
    winner = Label(frame, text="It's a tie!", font=("Arial", 25, "bold"), bg="white", fg="gray")
    winner.place(x=105, y=150)
game_over.mainloop()  

