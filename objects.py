import random

import pygame
from players import Player
from nps_class import Nps
from UI import UI

all_sprites = pygame.sprite.Group()

player = Player()
npsList = [Nps(), Nps()]
ui = UI()

#---------------------------------------

def create_nps(list):
    npsList.append(Nps())
    print('+++ CREATED')

    if random.randint(0,5) == 0:    # random increase nps
        create_nps(list)

def delete_nps(list):
    del list[0]
    print("--- OBJ IS DELETED")