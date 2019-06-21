#import os
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()

window = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Blob Game")

fruits = [pygame.image.load('strawberry.png')]
#bomb = pygame.image.load('__.jpg')
#bg = pygame.image.load('__.jpg')
basket = pygame.image.load('basket.png')

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
        while self.y < 800 + blob.height:
            self.y += self.vel

basket = Basket(250, 750)
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and blob.x > blob.vel:
        x -= vel
    if keys[pygame.K_RIGHT] and blob.x < 500 - blob.width - blob.vel:
        x += vel
