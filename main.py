import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()

display_width = 500
display_height = 800
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Fruit Catcher")

basket_img = pygame.image.load('basket.png')
basket_img = pygame.transform.scale(basket_img, (150, 100))
bg = pygame.image.load('background.jpg')
fruits_img = [pygame.image.load('strawberry.png')]
fruits_img[0] = pygame.transform.scale(fruits_img[0], (100, 100))
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
        self.vel = 1
    def draw(self, window):
        while self.y < 800:
            self.y += self.vel
            window.blit(fruits_img[0], (self.x, self.y))
            
def redrawGameWindow():
    window.blit(bg, (0,0))
    basket.draw(window)
    strawberry.draw(window)
    pygame.display.update()

#mainloop
basket = Basket(display_width * 0.35, display_height - 160)
strawberry = Fruits(display_width * 0.4, display_height * 0.1)
#pygame.time.set_timer(pygame.USEREVENT+1, 600) AFK option?
play = True
while play:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and basket.x > basket.vel - 5:
        basket.x -= basket.vel
    if keys[pygame.K_RIGHT] and basket.x < 500 - basket.width - basket.vel:
        basket.x += basket.vel
    
    redrawGameWindow()
pygame.quit()
