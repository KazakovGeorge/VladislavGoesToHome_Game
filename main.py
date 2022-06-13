import pygame
import random
import os
import math
import sys

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'player.png'))

background = pygame.image.load("images\\background.png")


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
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / random.randint(1, 10), HEIGHT - 200)

        self.speed = 1
        self.health = 100

    def health_update(self, heal):
        self.health += heal
        damage1.play()
        damage2.play()


    def walk_check(self):
        if self.rect.right > WIDTH:
            self.rect.x -= 50
            self.speed = self.speed * (-0.5)
            self.health_update(-20)

        if self.rect.left < 0:
            self.rect.x += 50
            self.speed = self.speed * (-0.5)
            self.health_update(-20)

    def update(self):
        player.rect.x += player.speed
        self.walk_check()



# Инициализация объектов
pygame.init()

pygame.mixer.init()  # для звука
pygame.mixer.music.load('sound1.mp3')
damage1 = pygame.mixer.Sound('damage1.wav')
damage2 = pygame.mixer.Sound('damage2.wav')
pygame.mixer.music.play()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VIIBLOCK Story")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group() # Группировка всех спрайтов

# Создание объектов мобов
player = Player()
all_sprites.add(player)



# Рабочий цикл
running =True
while running:
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed -= 5
            elif event.key == pygame.K_RIGHT:
                player.speed += 5


    # Обновление
    all_sprites.update()

    # Визуализация (сборка)
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # Переворот экрана
    pygame.display.flip()

    print(pygame.time.get_ticks()/1000, ' \\ Health: ', player.health)