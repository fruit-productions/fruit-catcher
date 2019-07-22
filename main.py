import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import time
import random

pygame.init()

display_width = 500
display_height = 800
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Fruit Catcher")

basket_img = pygame.image.load('basket.png')
basket_img = pygame.transform.scale(basket_img, (150, 100))
bg = pygame.image.load('background.jpg')
bomb_img = pygame.image.load('bomb.png')
bomb_img = pygame.transform.scale(bomb_img, (100, 100))

clock = pygame.time.Clock()

class Basket(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
    def draw(self, window):
        window.blit(basket_img, (self.x, self.y))
    
class Fruits(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
    def draw(self, num, window):
        if num == 0:
            fruit = pygame.image.load('strawberry.png')
        fruit = pygame.transform.scale(fruit, (100, 100))
        window.blit(fruit, (self.x, self.y))
        # add more fruits later
    def collision():
        pass

def main():
    basket = Basket(display_width * 0.35, display_height - 160)
    fruit_startx = random.randrange(100, display_width - 100)
    fruit_starty = 0
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.x > basket.vel - 5:
            basket.x -= basket.vel
        if keys[pygame.K_RIGHT] and basket.x < 500 - 150 - basket.vel:
            basket.x += basket.vel
        window.blit(bg, (0,0))
        strawberry = Fruits(fruit_startx, fruit_starty)
        strawberry.draw(0, window)
        fruit_starty += strawberry.vel
        basket.draw(window)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

main()
