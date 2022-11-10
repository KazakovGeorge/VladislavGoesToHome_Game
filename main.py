import pygame
from objects import player, npsList, ui
import os
import config, events
from objects import all_sprites

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'player.png'))

background = pygame.image.load("images\\background.png")

# Инициализация объектов
pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("VIIBLOCK Story")
clock = pygame.time.Clock()

#all_sprites = pygame.sprite.Group() # Группировка всех спрайтов

# Создание объектов мобов

all_sprites.add(player)   # load thePlayer sprite
all_sprites.add(npsList)
all_sprites.add(ui) # load nps sprites

# Рабочий цикл
running = True  # True если игра работает

while running:
    clock.tick(config.FPS)

    # Ввод процесса (события)
    running = events.check_all(running) # Запуск функции проверки событий и возвращение закрытия игры, если требуется
    player.chek_collizions(npsList)

    # Обновление
    ui.update_health(player.health)

    all_sprites.add(npsList)
    all_sprites.update()

    # Визуализация (сборка)
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # Переворот экрана
    pygame.display.flip()

    print(f"{clock.tick()} | {len(npsList)}")