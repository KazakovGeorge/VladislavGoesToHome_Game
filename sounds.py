import pygame

pygame.mixer.init()  # для звука
pygame.mixer.music.load('sounds\sound1.mp3')

playerDamage1 = pygame.mixer.Sound('sounds\damage1.wav')
playerDamage2 = pygame.mixer.Sound('sounds\damage2.wav')

#npsDamage_1 = pygame.mixer.Sound(f'sounds/nps/damage_{random.randint(1,3)}.mp3')

pygame.mixer.music.play()
pygame.mixer.music.set_volume(10)