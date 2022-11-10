import datetime

import pygame
import random
import os, math
import config, sounds

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'player.png'))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(config.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / random.randint(1, 10), config.HEIGHT * 0.9)

        self.speed = 1
        self.health = 100

    def update(self):
        self.rect.x += self.speed
        #self.rect.y = config.HEIGHT * 0.75
        self.walk_check()


    def health_update(self, heal):
        self.health += heal
        sounds.damage1.play()
        sounds.damage2.play()


    def walk_check(self):
        if self.rect.right > config.WIDTH:
            self.rect.x -= 50
            self.speed = self.speed * (-0.5)
            self.health_update(-10)
            print(pygame.time.get_ticks() / 1000, ' \\ Health: ', self.health)

        if self.rect.left < 0:
            self.rect.x += 50
            self.speed = self.speed * (-0.5)
            self.health_update(-10)
            print(pygame.time.get_ticks() / 1000, ' \\ Health: ', self.health)


    def chek_collizions(self, list : list):
        for nps in list:
            if self.rect.colliderect(nps.rect):
                nps.health_update(-20)
                nps.rect.y += -100
                print("COLIDE")
                sounds.damage1.play()
