#import os
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()

window = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Fruit Catcher")

fruits = [pygame.image.load('strawberry.png')]
bomb = pygame.image.load('bomb.png')
bg = pygame.image.load('background.jpg')
basket_img = pygame.image.load('basket.png')

clock = pygame.time.Clock()
fruit_count = 0
max_fruit = 5

class Basket(object):
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
        while self.y < 800 + basket.height:
            self.y += self.vel

def redrawGameWindow():
    #win.blit(bg, (0,0))
    if (fruit_count < max_fruit):
        win.blit(basket[fruit_count], (x,y))
    else:
        win.blit(basket[max_fruit], (x,y))
    pygame.display.update()
    
basket = Basket(250, 750, 30, 30)

play = True
while play:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and basket.x > basket.vel:
        basket.x -= basket.vel
    if keys[pygame.K_RIGHT] and basket.x < 500 - basket.width - basket.vel:
        basket.x += basket.vel 
    #if (basket catches fruit): increase fruit_count
       
redrawGameWindow()
