import pygame, os
import config

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images\\numbers')
#player_img = pygame.image.load(os.path.join(img_folder, '0.png'))

class UI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, str('10.png')))
        self.image.set_colorkey(config.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH * 0.9, config.HEIGHT * 0.2)

        self.level = 0

    def update(self):
        self.update_image()
        pass

    def update_image(self):
        if self.level >= 0:
            self.image = self.image = pygame.image.load(os.path.join(img_folder, str(f'{int(self.level)}.png')))

    def update_health(self, newLevel : int):
        self.level = (newLevel / 10) - (newLevel % 10)
