import pygame
import random
import os
import config, sounds, objects

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
#player_img = pygame.image.load(os.path.join(img_folder, str(f'Cizen_{random.randint(1,11)}.png')))

#----------------------------------------------------------------------------------------------------------------------

class Nps(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, str(f'nps/Cizen_{random.randint(1,11)}.png')))
        self.image.set_colorkey(config.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, config.WIDTH-50), -500)

        self.speed = 2
        self.health = 100


    def update(self):
        self.rect.y += self.speed

        self.walk_check()
        self.chek_collizions()


    def health_update(self, heal):
        self.health += heal
        if self.health < 1:
            self.kill()


    def walk_check(self):
        if self.rect.bottom > config.HEIGHT + 500:
            self.kill()

    def chek_collizions(self):
        for obj in objects.all_sprites:
            if obj.__str__() != '<Nps Sprite(in 1 groups)>':

                if obj.__str__() == '<Bullet Sprite(in 1 groups)>' and self.rect.colliderect(obj.rect) == True:
                    obj.kill()
                    self.health_update(-30)
                    self.rect.y += -100
                    sounds.pygame.mixer.Sound(f'sounds/nps/damage_{random.randint(1,3)}.mp3').play()

#----------------------------------------------------------------------------------------------------------------------

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'bullets', str(f'Bullet_{random.randint(1,3)}.png')))
        self.image.set_colorkey(config.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = objects.player.rect.midtop

        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        self.walk_check()

    def walk_check(self):
        if self.rect.top < -500:
            self.kill()


