import pygame
import random
import math

class Player():
    def __init__(self, x, y,circles, score=0,bullets=10,shotgun_bullets=0):
        self.x = x
        self.y = y
        self.score = score
        self.bullets = bullets
        self.circles = circles
        self.shotgun_bullets = shotgun_bullets

class Target():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

class SpecialTarget(Target):
    def __init__(self, x, y, image,start_time,interval):
        super().__init__(x, y, image)
        self.show = False
        self.start_time = start_time
        self.show_duration = 4000
        self.interval = interval  

    def update(self):
        current_time = pygame.time.get_ticks()
        
        if not self.show and current_time - self.start_time >= self.interval:
            self.show = True
            self.start_time = current_time  
            self.x = random.randint(0, 750)
            self.y = random.randint(0, 550)

        if self.show and current_time - self.start_time >= self.show_duration:
            self.show = False

    def render(self, screen):
        if self.show:
            screen.blit(self.image, (self.x, self.y))

last_shot1 = [0, 0]
last_shot2 = [0, 0]

def distance(x1, x2, y1, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    score_plus = int(distance/100)
    score_plus += 1
    return score_plus

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('CShot')
icon = pygame.image.load("shooting-range.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load('target.png')
target_image = pygame.transform.scale(target_image, (50, 50))
shotgun_bullet_image = pygame.image.load('shotgun_bullets.png')
shotgun_bullet_image = pygame.transform.scale(shotgun_bullet_image, (50, 50))
extra_ammo_image = pygame.image.load('extra_ammo.png')
extra_ammo_image = pygame.transform.scale(extra_ammo_image, (50, 50))
double_points_image = pygame.image.load('double-points.png')
double_points_image = pygame.transform.scale(double_points_image, (50, 50))

player1 = Player(random.randint(0, 775), random.randint(0, 575),circles=[])
player2 = Player(random.randint(0, 775), random.randint(0, 575),circles=[])

def player(player):
    screen.blit(screen,(player.x, player.y))

target1 = Target(random.randint(0, 750), random.randint(0, 550), target_image)
target2 = Target(random.randint(0, 750), random.randint(0, 550), target_image)
target3 = Target(random.randint(0, 750), random.randint(0, 550), target_image)

special_target1 = SpecialTarget(random.randint(0, 750), random.randint(0, 550), shotgun_bullet_image,start_time=0,interval=5000)
special_target2 = SpecialTarget(random.randint(0, 750), random.randint(0, 550), extra_ammo_image,start_time=0,interval=7000)
special_target3 = SpecialTarget(random.randint(0, 750), random.randint(0, 550), double_points_image,start_time=0,interval=13000)

xchange1, ychange1 = 0, 0
xchange2, ychange2 = 0, 0

pygame.init()
font = pygame.font.Font(None, 20)
start_time = pygame.time.get_ticks()
game_duration = 100000



running = True
while running:
    screen.fill((255, 255, 255))
    player(player1)
    player(player2)
    elapsed_time = pygame.time.get_ticks() - start_time
    remaining_time = max(0, (game_duration - elapsed_time) // 1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ychange1 = -0.2
            if event.key == pygame.K_s:
                ychange1 = 0.2
            if event.key == pygame.K_a:
                xchange1 = -0.2
            if event.key == pygame.K_d:
                xchange1 = 0.2

            if event.key == pygame.K_UP:
                ychange2 = -0.2
            if event.key == pygame.K_DOWN:
                ychange2 = 0.2
            if event.key == pygame.K_LEFT:
                xchange2 = -0.2
            if event.key == pygame.K_RIGHT:
                xchange2 = 0.2
            
            if event.key == pygame.K_TAB:
                if player1.bullets > 0:
                    if player1.shotgun_bullets > 0:
                        player1.bullets -= 1
                        player1.shotgun_bullets -= 1
                        pygame.mixer.music.load('shotgun1.wav')
                        pygame.mixer.music.play()
                        player1.circles.append([(player1.x, player1.y),(player1.x+10, player1.y),(player1.x-10, player1.y),(player1.x, player1.y-10),(player1.x, player1.y+10),(player1.x+8,player1.y-7),(player1.x+6,player1.y+4),(player1.x-3,player1.y-8),(player1.x-4,player1.y+4),(player1.x-2,player1.y-2),(player1.x+2,player1.y-6),(player1.x+6,player1.y+7),(player1.x-7,player1.y-6),(player1.x+5,player1.y)])
                    else:
                        player1.bullets -= 1
                        pygame.mixer.music.load('bullet1.wav')
                        pygame.mixer.music.play()
                        player1.circles.append((player1.x, player1.y))
                        
                    for target in [target1, target2, target3]:
                        if player1.shotgun_bullets > 0:
                            if target.x - 10 < player1.x < target.x + 60 and target.y - 10 < player1.y < target.y + 60:
                                pygame.mixer.music.load('vay-hossein.wav')
                                pygame.mixer.music.play()
                                player1.score += distance(player1.x, last_shot1[0],player1.y, last_shot1[1])
                                target.x = random.randint(0, 750)
                                target.y = random.randint(0, 550)
                        else:
                            if target.x < player1.x < target.x + 50 and target.y < player1.y < target.y + 50:
                                pygame.mixer.music.load('vay-hossein.wav')
                                pygame.mixer.music.play()
                                player1.score += distance(player1.x, last_shot1[0],player1.y, last_shot1[1])
                                target.x = random.randint(0, 750)
                                target.y = random.randint(0, 550)
                    if player1.shotgun_bullets > 0:
                        if special_target1.x - 10 < player1.x < special_target1.x + 60 and special_target1.y - 10 < player1.y < special_target1.y + 60:
                            player1.shotgun_bullets += 3
                            player1.bullets += 3
                            player1.score += distance(player1.x, last_shot1[0],player1.y, last_shot1[1])
                            pygame.mixer.music.load('reload.mp3')
                            pygame.mixer.music.play()
                            special_target1.show = False
                        if special_target2.x - 10 < player1.x < special_target2.x + 60 and special_target2.y - 10 < player1.y < special_target2.y + 60:
                            player1.bullets += 10
                            player1.score += distance(player1.x, last_shot1[0],player1.y, last_shot1[1])
                            special_target2.show = False
                        if special_target3.x - 10 < player1.x < special_target3.x + 60 and special_target3.y - 10 < player1.y < special_target3.y + 60:
                            player1.score *= 2
                            pygame.mixer.music.load('2x.mp3')
                            pygame.mixer.music.play()
                            special_target3.show = False
                    else:
                        if special_target1.x < player1.x < special_target1.x + 50 and special_target1.y < player1.y < special_target1.y + 50:
                            player1.shotgun_bullets += 3
                            player1.bullets += 3
                            player1.score += distance(player1.x, last_shot1[0],player1.y, last_shot1[1])
                            pygame.mixer.music.load('reload.mp3')
                            pygame.mixer.music.play()
                            special_target1.show = False
                        if special_target2.x < player1.x < special_target2.x + 50 and special_target2.y < player1.y < special_target2.y + 50:
                            player1.bullets += 10
                            player1.score += distance(player1.x, last_shot1[0],player1.y, last_shot1[1])
                            special_target2.show = False
                        if special_target3.x < player1.x < special_target3.x + 50 and special_target3.y < player1.y < special_target3.y + 50:
                            player1.score *= 2
                            pygame.mixer.music.load('2x.mp3')
                            pygame.mixer.music.play()
                            special_target3.show = False
                    last_shot1[0] = player1.x
                    last_shot1[1] = player1.y

            if event.key == pygame.K_RETURN:
                if player2.bullets > 0:
                    if player2.shotgun_bullets > 0:
                        player2.bullets -= 1
                        player2.shotgun_bullets -= 1
                        pygame.mixer.music.load("shotgun2.wav")
                        pygame.mixer.music.play()
                        player2.circles.append([(player2.x, player2.y),(player2.x+10, player2.y),(player2.x-10, player2.y),(player2.x, player2.y-10),(player2.x, player2.y+10),(player2.x+8,player2.y-7),(player2.x+6,player2.y+4),(player2.x-3,player2.y-8),(player2.x-4,player2.y+4),(player2.x-2,player2.y-2),(player2.x+2,player2.y-6),(player2.x+6,player2.y+7),(player2.x-7,player2.y-6),(player2.x+5,player2.y)])
                    else:
                        player2.bullets -= 1
                        pygame.mixer.music.load('bullet2.wav')
                        pygame.mixer.music.play()
                        player2.circles.append((player2.x, player2.y))
                    for target in [target1, target2, target3]:
                        if player2.shotgun_bullets > 0:
                            if target.x - 10 < player2.x < target.x + 60 and target.y - 10 < player2.y < target.y + 60:
                                player2.score += distance(player2.x, last_shot2[0],player2.y, last_shot2[1])
                                pygame.mixer.music.load('vay-hossein.wav')
                                pygame.mixer.music.play()
                                target.x = random.randint(0, 750)
                                target.y = random.randint(0, 550)
                        else:
                            if target.x < player2.x < target.x + 50 and target.y < player2.y < target.y + 50:
                                player2.score += distance(player2.x, last_shot2[0],player2.y, last_shot2[1])
                                pygame.mixer.music.load('vay-hossein.wav')
                                pygame.mixer.music.play()
                                target.x = random.randint(0, 750)
                                target.y = random.randint(0, 550)
                    if player2.shotgun_bullets > 0:
                        if special_target1.x - 10 < player2.x < special_target1.x + 60 and special_target1.y - 10 < player2.y < special_target1.y + 60:
                            player2.shotgun_bullets += 3
                            player2.bullets += 3
                            player2.score += distance(player2.x, last_shot2[0],player2.y, last_shot2[1])
                            pygame.mixer.music.load('reload.mp3')
                            pygame.mixer.music.play()
                            special_target1.show = False
                        if special_target2.x - 10 < player2.x < special_target2.x + 60 and special_target2.y - 10 < player2.y < special_target2.y + 60:
                            player2.bullets += 10
                            player2.score += distance(player2.x, last_shot2[0],player2.y, last_shot2[1])
                            special_target2.show = False
                        if special_target3.x - 10 < player2.x < special_target3.x + 60 and special_target3.y - 10 < player2.y < special_target3.y + 60:
                            player2.score *= 2
                            pygame.mixer.music.load('2x.mp3')
                            pygame.mixer.music.play()
                            special_target3.show = False
                    else:
                        if special_target1.x < player2.x < special_target1.x + 50 and special_target1.y < player2.y < special_target1.y + 50:
                            player2.shotgun_bullets += 3
                            player2.bullets += 3
                            player2.score += distance(player2.x, last_shot2[0],player2.y, last_shot2[1])
                            pygame.mixer.music.load('reload.mp3')
                            pygame.mixer.music.play()
                            special_target1.show = False
                        if special_target2.x < player2.x < special_target2.x + 50 and special_target2.y < player2.y < special_target2.y + 50:
                            player2.bullets += 10
                            player2.score += distance(player2.x, last_shot2[0],player2.y, last_shot2[1])
                            special_target2.show = False
                        if special_target3.x < player2.x < special_target3.x + 50 and special_target3.y < player2.y < special_target3.y + 50:
                            player2.score *= 2
                            pygame.mixer.music.load('2x.mp3')
                            pygame.mixer.music.play()
                            special_target3.show = False
                    last_shot2[0] = player2.x
                    last_shot2[1] = player2.y

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                xchange1 = 0
            if event.key in [pygame.K_w, pygame.K_s]:
                ychange1 = 0
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                xchange2 = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                ychange2 = 0
        
    player1.x = max(0, min(player1.x + xchange1, 775))
    player1.y = max(0, min(player1.y + ychange1, 575))
    player2.x = max(0, min(player2.x + xchange2, 775))
    player2.y = max(0, min(player2.y + ychange2, 575))

    for target_obj in [target1, target2, target3, special_target1, special_target2, special_target3]:
        target_obj.render(screen)

    for circle in player1.circles:
        if type(circle) == tuple:
            pygame.draw.circle(screen, (255, 0, 0), circle, 2)
        else:
            for i in circle:
                pygame.draw.circle(screen, (255, 0, 0), i, 3)
    for circle in player2.circles:
        if type(circle) == tuple:
            pygame.draw.circle(screen, (0, 0, 255), circle, 2)
        else:
            for j in circle:
                pygame.draw.circle(screen, (0, 0, 255), j, 3)


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

    pygame.display.update()
    
    for special_target in [special_target1, special_target2, special_target3]:
        special_target.update()

pygame.quit()