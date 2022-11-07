import pygame

import objects
from objects import player, npsList

def check_all(running : bool):
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.speed -= 5
            elif event.key == pygame.K_RIGHT:
                player.speed += 5

            elif event.key == pygame.K_n:
                objects.create_nps(npsList)
            elif event.key == pygame.K_p:
                if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()


    return running