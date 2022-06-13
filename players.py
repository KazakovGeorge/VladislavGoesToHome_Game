import pygame
import random
import os
import math
import sys

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'player.png'))

WIDTH = 1920
HEIGHT = 1080
FPS = 60

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / random.randint(1,10), HEIGHT / random.randint(1,10))
        self.speed = 2


    def update(self):