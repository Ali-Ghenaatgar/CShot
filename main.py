import pygame
import random
import time

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

class ShotgunBullet(Target):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.show = False
        self.start_time = 0
        self.show_duration = 2000
        self.interval = 5000  

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

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('CShot')

font = pygame.font.Font(None, 20)

target_image = pygame.image.load('target.png')
target_image = pygame.transform.scale(target_image, (50, 50))
shotgun_bullet_image = pygame.image.load('shotgun_bullets.png')
shotgun_bullet_image = pygame.transform.scale(shotgun_bullet_image, (50, 50))

player1 = Player(random.randint(0, 775), random.randint(0, 575),circles=[])
player2 = Player(random.randint(0, 775), random.randint(0, 575),circles=[])

def player(player):
    screen.blit(screen,(player.x, player.y))

target1 = Target(random.randint(0, 750), random.randint(0, 550), target_image)
target2 = Target(random.randint(0, 750), random.randint(0, 550), target_image)
target3 = Target(random.randint(0, 750), random.randint(0, 550), target_image)
special_target1 = ShotgunBullet(random.randint(0, 750), random.randint(0, 550), shotgun_bullet_image)

xchange1, ychange1 = 0, 0
xchange2, ychange2 = 0, 0

running = True
while running:
    screen.fill((255, 255, 255))
    player(player1)
    player(player2)
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
                        player1.circles.append([(player1.x, player1.y)])
                    else:
                        player1.bullets -= 1
                        pygame.mixer.music.load('bullet1.wav')
                        pygame.mixer.music.play()
                        player1.circles.append((player1.x, player1.y))
                        
                    for target in [target1, target2, target3]:
                        if player1.shotgun_bullets > 0:
                            if target.x - 25 < player1.x < target.x + 75 and target.y - 25 < player1.y < target.y + 75:
                                pygame.mixer.music.load('vay-hossein.wav')
                                pygame.mixer.music.play()
                                player1.score += 1
                                target.x = random.randint(0, 750)
                                target.y = random.randint(0, 550)
                        else:
                            if target.x < player1.x < target.x + 50 and target.y < player1.y < target.y + 50:
                                pygame.mixer.music.load('vay-hossein.wav')
                                pygame.mixer.music.play()
                                player1.score += 1
                                target.x = random.randint(0, 750)
                                target.y = random.randint(0, 550)

                    if special_target1.x < player1.x < special_target1.x + 50 and special_target1.y < player1.y < special_target1.y + 50:
                        player1.shotgun_bullets += 3
                        player1.bullets += 3
                        special_target1.x = random.randint(0, 750)
                        special_target1.y = random.randint(0, 550)

            if event.key == pygame.K_RETURN:
                if player2.bullets > 0:
                    if player2.shotgun_bullets > 0:
                        player2.bullets -= 1
                        player2.shotgun_bullets -= 1
                        pygame.mixer.music.load("shotgun2.wav")
                        pygame.mixer.music.play()
                        player2.circles.append([(player2.x, player2.y)])
                    else:
                        player2.bullets -= 1
                        pygame.mixer.music.load('bullet2.wav')
                        pygame.mixer.music.play()
                        player2.circles.append((player2.x, player2.y))
                    for target in [target1, target2, target3]:
                        if player2.shotgun_bullets > 0:
                            if target.x - 25 < player2.x < target.x + 75 and target.y - 25 < player2.y < target.y + 75:
                                player2.score += 1
                                pygame.mixer.music.load('vay-hossein.wav')
                                pygame.mixer.music.play()
                                target.x = random.randint(0, 750)
                                target.y = random.randint(0, 550)
                        else:
                            if target.x < player2.x < target.x + 50 and target.y < player2.y < target.y + 50:
                                player2.score += 1
                                pygame.mixer.music.load('vay-hossein.wav')
                                pygame.mixer.music.play()
                                target.x = random.randint(0, 750)
                                target.y = random.randint(0, 550)
                    if special_target1.x < player2.x < special_target1.x + 50 and special_target1.y < player2.y < special_target1.y + 50:
                        player2.shotgun_bullets += 3
                        player2.bullets += 3
                        special_target1.x = random.randint(0, 750)
                        special_target1.y = random.randint(0, 550)

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

    for target_obj in [target1, target2, target3, special_target1]:
        target_obj.render(screen)

    for circle in player1.circles:
        if type(circle) == tuple:
            pygame.draw.circle(screen, (255, 0, 0), circle, 2)
        else:
            pygame.draw.circle(screen, (255, 0, 0), circle[0], 25)
    for circle in player2.circles:
        if type(circle) == tuple:
            pygame.draw.circle(screen, (0, 0, 255), circle, 2)
        else:
            pygame.draw.circle(screen, (0, 0, 255), circle[0], 25)

    score_text1 = font.render(f"Player 1: {player1.score}", True, (0, 0, 0))
    score_text2 = font.render(f"Player 2: {player2.score}", True, (0, 0, 0))
    remaining_bullets1 = font.render(f"Player 1 Bullets: {player1.bullets}", True, (0, 0, 0)) if player1.bullets > 0 else font.render(f"Player 1 Bullets: {player1.bullets}", True, (255, 0, 0))
    remaining_bullets2 = font.render(f"Player 2 Bullets: {player2.bullets}", True, (0, 0, 0)) if player2.bullets > 0 else font.render(f"Player 2 Bullets: {player2.bullets}", True, (255, 0, 0))

    screen.blit(score_text1, (10, 10))
    screen.blit(score_text2, (10, 30))
    screen.blit(remaining_bullets1, (10, 50))
    screen.blit(remaining_bullets2, (10, 70))

    pygame.display.update()
    special_target1.update()
pygame.quit()