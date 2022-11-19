import pygame, random
import nps_class, objects, sounds
from objects import player


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

            elif event.key == pygame.K_SPACE:
                sounds.pygame.mixer.Sound(f'sounds/player/toss_{random.randint(1, 2)}.wav').play()
                objects.all_sprites.add(nps_class.Bullet())

            elif event.key == pygame.K_n:
                objects.all_sprites.add(nps_class.Nps())

            elif event.key == pygame.K_p:
                if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_o:
                print(f'{len(objects.all_sprites.sprites())} : {objects.all_sprites.sprites()}')


    return running