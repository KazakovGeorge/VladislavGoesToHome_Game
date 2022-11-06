import pygame

pygame.mixer.init()  # для звука
pygame.mixer.music.load('sound1.mp3')
damage1 = pygame.mixer.Sound('damage1.wav')
damage2 = pygame.mixer.Sound('damage2.wav')

pygame.mixer.music.play()
pygame.mixer.music.set_volume(10)