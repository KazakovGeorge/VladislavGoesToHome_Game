import pygame
from objects import player, npsList
import os
import config, events

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'player.png'))

background = pygame.image.load("images\\background.png")

# Инициализация объектов
pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("VIIBLOCK Story")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group() # Группировка всех спрайтов

# Создание объектов мобов

all_sprites.add(player)   # load thePlayer sprite
all_sprites.add(npsList)  # load nps sprites

# Рабочий цикл
running = True  # True если игра работает

while running:
    clock.tick(config.FPS)

    # Ввод процесса (события)
    running = events.check_all(running) # Запуск функции проверки событий и возвращение закрытия игры, если требуется

    # Обновление
    all_sprites.update()

    # Визуализация (сборка)
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # Переворот экрана
    pygame.display.flip()