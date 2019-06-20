#import os
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()

window = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Blob Game")

#fruits = [LIST OF IMAGES OF FRUITS, pygame.image.load('__.jpg')]
#bomb = pygame.image.load('__.jpg')
#bg = pygame.image.load('__.jpg')
#char = pygame.image.load('___.jpg')
#basket = [LIST OF IMAGES OF BASKETS WITH FRUITS, pygame.image.load('___.jpg)]

clock = pygame.time.Clock()
fruit_count = 0
max_fruit = 5

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

class Fruit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
    def appear(self, x, y):
        # draw fruit at coordinates (x,y)
        while self.y < 800 + blob.height:
            self.y += self.vel

def redrawGameWindow():
    #win.blit(bg, (0,0))
    if (fruit_count < max_fruit):
        win.blit(basket[fruit_count], (x,y))
    else:
        win.blit(basket[max_fruit], (x,y))
    pygame.display.update()
    
basket = Player(250, 750)
play = True
while play:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and basket.x > basket.vel:
        x -= vel
    if keys[pygame.K_RIGHT] and basket.x < 500 - basket.width - basket.vel:
        x += vel   
    #if (basket catches fruit): increase fruit_count
       
redrawGameWindow()
