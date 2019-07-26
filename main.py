import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import time
import random

pygame.init()

display_width = 500
display_height = 800
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Basket Game")

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
        self.hitbox = (self.x, self.y + 20, 150, 80)
    def draw(self, window):
        window.blit(basket_img, (self.x, self.y))
        self.hitbox = (self.x, self.y + 20, 150, 80)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    
class Fruits(object):
    def __init__(self, x, y, f_type):
        self.x = x
        self.y = y
        self.vel = 20
        self.f_type = f_type
        self.hitbox = (self.x, self.y, 100, 100)
    def draw(self, window):
        if self.f_type == 0:
            fruit = pygame.image.load('strawberry.png')
        fruit = pygame.transform.scale(fruit, (100, 100))
        window.blit(fruit, (self.x, self.y))
        self.hitbox = (self.x, self.y, 100, 100)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

def main():
    score = 0
    fruits = []
    fruit_add_counter = 0
    add_fruit_rate = 20
    basket = Basket(display_width * 0.35, display_height - 160)
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False      
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.x > basket.vel - 5:
            basket.x -= basket.vel
        elif keys[pygame.K_RIGHT] and basket.x < 500 - 150 - basket.vel:
            basket.x += basket.vel  
        window.blit(bg, (0,0))
        fruit_add_counter += 1
        if fruit_add_counter == add_fruit_rate:
            fruit_add_counter = 0
            f_startx = random.randrange(100, display_width - 100)
            f_starty = 0
            f_type = 0 # change to random later
            new_fruit = Fruits(f_startx, f_starty, f_type)
            fruits.append(new_fruit)
        for item in fruits:
            item.draw(window)
            item.y += item.vel
        for item in fruits[:]:
            if (item.hitbox[0] >= basket.hitbox[0] - 20) and (item.hitbox[0] <= basket.hitbox[0] + 70):
                if basket.hitbox[1] - 120 <= item.hitbox[1] <= basket.hitbox[1] - 40:
                    fruits.remove(item)
                    score += 1
                    print("Score:", score)
        basket.draw(window)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

main()
