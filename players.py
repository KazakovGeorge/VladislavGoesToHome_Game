import pygame
import random
import os
import config, sounds
import objects

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

        self.walk_check()
        self.chek_collizions()


    def health_update(self, heal):
        self.health += heal
        sounds.playerDamage1.play()
        sounds.playerDamage2.play()


    def walk_check(self):
        if self.rect.right > config.WIDTH:
            self.rect.x -= 50
            self.speed = self.speed * (-0.5)
            self.health_update(-10)

        if self.rect.left < 0:
            self.rect.x += 50
            self.speed = self.speed * (-0.5)
            self.health_update(-10)


    def chek_collizions(self):
        for nps in objects.all_sprites:
            if nps.__str__() != '<Player Sprite(in 1 groups)>':

                if nps.__str__() == '<Nps Sprite(in 1 groups)>' and self.rect.colliderect(nps.rect) == True:
                    nps.health_update(-20)
                    objects.player.health_update(-10)
                    nps.rect.y += -100
                    sounds.playerDamage1.play()



    """def chek_collizions(self, list : list):
        for nps in list:
            if self.rect.colliderect(nps.rect):
                nps.health_update(-20)
                nps.rect.y += -100
                print("COLIDE")
                sounds.damage1.play()"""
