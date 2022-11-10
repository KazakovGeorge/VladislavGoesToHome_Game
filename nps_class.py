import pygame
import random
import os
import config, sounds, objects

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images/nps')
player_img = pygame.image.load(os.path.join(img_folder, str(f'Cizen_{random.randint(1,11)}.png')))

class Nps(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, str(f'Cizen_{random.randint(1,11)}.png')))
        self.image.set_colorkey(config.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / random.randint(1, 10), -500)

        self.speed = 4
        self.health = 100


    def update(self):
        self.rect.y += self.speed
        self.walk_check()


    def health_update(self, heal):
        if self.health < 1:
            for i in range(len(objects.npsList)):
                if objects.npsList[i] == self:
                    objects.npsList[i].kill()
                    del objects.npsList[i]
                    del self
        else:
            self.health += heal


    def walk_check(self):
        if self.rect.bottom > config.HEIGHT + 500:
            self.kill()
            objects.delete_nps(objects.npsList)
            objects.create_nps(objects.npsList)


        """if self.rect.top < (-500):
            self.kill()
            objects.create_nps(objects.npsList)"""


