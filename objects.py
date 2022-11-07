import random

import pygame
from players import Player
from nps_class import Nps

player = Player()

npsList = [Nps()]

def create_nps(list):
    print('+++ CREATED')
    npsList.append(Nps())

    if random.randint(0,5) == 0:
        create_nps(list)

def delete_nps(list):
    del list[0]
    print("--- OBJ IS DELETED")