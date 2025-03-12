import pygame
import random

class Player():
    def __init__(self, x, y, image, score):
        self.x = x
        self.y = y
        self.image = image
        self.score = score

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('CShot')

image1 = pygame.image.load('arrow.png')
image1 = pygame.transform.scale(image1, (25, 25))

player1 = Player(random.randint(0, 775), random.randint(0, 575), image1, score=0)
player2 = Player(random.randint(0, 775), random.randint(0, 575), image1, score=0)

def player(image, x, y):
    screen.blit(image, (x, y))

xchange1, ychange1 = 0, 0
xchange2, ychange2 = 0, 0

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ychange1 = -0.1
            if event.key == pygame.K_s:
                ychange1 = 0.1
            if event.key == pygame.K_a:
                xchange1 = -0.1
            if event.key == pygame.K_d:
                xchange1 = 0.1

            if event.key == pygame.K_UP:
                ychange2 = -0.1
            if event.key == pygame.K_DOWN:
                ychange2 = 0.1
            if event.key == pygame.K_LEFT:
                xchange2 = -0.1
            if event.key == pygame.K_RIGHT:
                xchange2 = 0.1

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

    player(player1.image, player1.x, player1.y)
    player(player2.image, player2.x, player2.y)

    pygame.display.update()

pygame.quit()