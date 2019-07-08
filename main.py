#import os
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()

window = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Fruit Catcher")

fruits = [pygame.image.load('strawberry.png')]
#bomb = pygame.image.load('__.jpg')
#bg = pygame.image.load('__.jpg')
basket_img = pygame.image.load('basket.png')

score = 0
class Basket(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.hitbox = (self.x + 20, self.y, 30, 60) #x,y,width,height//temp values
  
class Fruit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.hitbox = (self.x + 20, self.y, 30, 60) #temp values
    def appear(self, x, y):
        # draw fruit at coordinates (x,y)
        while self.y < 800 + basket.height:
            self.y += self.vel
    def hit(self):
        print("You caught a fruit!")
        score += 10 #temp value
        #function for making the fruit disappear once caught
        pass

basket = Basket(250, 750, 30, 30)
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and basket.x > basket.vel:
        basket.x -= basket.vel
        #if (basket.x < fruit.hitbox[0 + width]):
        #   fruit.hit()
    if keys[pygame.K_RIGHT] and basket.x < 500 - basket.width - basket.vel:
        basket.x += basket.vel
        #if (basket.x > fruit.hitbox[1+height]):
