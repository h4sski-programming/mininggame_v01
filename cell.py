import pygame
from random import random

from settings import CELL_SIZE, HEIGHT

types: dict ={
    'surface':  {'colour': 'green',     'rarity': 1,    'minimum_depth': 0,     'hp': 0},
    'tunnel':   {'colour': 'yellow',    'rarity': 1,    'minimum_depth': 0,     'hp': 0},
    'soil':     {'colour': 'brown',     'rarity': 1,    'minimum_depth': 0,     'hp': 3},
    'coal':     {'colour': 'black',     'rarity': 12,   'minimum_depth': 0.2,   'hp': 5},
    'iron':     {'colour': 'purple',    'rarity': 30,   'minimum_depth': 0.4,   'hp': 8},
    'diamond':  {'colour': 'blue', 'rarity': 50,   'minimum_depth': 0.7,   'hp': 13},
}

# class Cell_type():
#     def __init__(self, type: str) -> None:
#         print(f'{types = }')
#         # if type in types:
#         #     pass
#         self.type = type
#         self.colour = types[self.type]['colour']
#         self.rarity = types[self.type]['rarity']
#         self.minimum_depth = types[self.type]['minimum_depth']
#         self.hp = types[self.type]['hp']

class Cell():
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.position: list = [x, y]
        self.hp = 0
        if self.y == 0:
            self.type: str = 'surface'
            self.colour: str = 'green'
            self.discovered: bool = True
        else:
            rand = random()
            # print(f'{rand = }')
            self.discovered: bool = False
            if rand <= 1 / types['diamond']['rarity'] and y >= HEIGHT * types['diamond']['minimum_depth']:
                # print(f"Diamont {rand = }, {types['diamond']['rarity'] = }")
                self.type: str = 'diamond'
                self.colour: str = types['diamond']['colour']
                self.hp: int = types['diamond']['hp']
            elif rand <= 1 / types['iron']['rarity'] and y >= HEIGHT * types['iron']['minimum_depth']:
                self.type: str = 'iron'
                self.colour: str = types['iron']['colour']
                self.hp: int = types['iron']['hp']
            elif rand <= 1 / types['coal']['rarity'] and y >= HEIGHT * types['coal']['minimum_depth']:
                self.type: str = 'coal'
                self.colour: str = types['coal']['colour']
                self.hp: int = types['coal']['hp']
            else:
                self.type: str = 'soil'
                self.colour: str = types['soil']['colour']
                self.hp: int = types['soil']['hp']
    
    
    def draw(self, surface):
        if self.type == 'surface':
            pygame.draw.rect(surface, self.colour, (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)
        # else:
        if self.discovered:
            if self.hp > 0:
                # pygame.draw.rect(surface, 'yellow', (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)
                pygame.draw.rect(surface, self.colour, (self.x, self.y, CELL_SIZE, CELL_SIZE), self.hp * 2)
                # pygame.draw.circle(surface, self.colour, (self.x + CELL_SIZE/2, self.y + CELL_SIZE/2), (CELL_SIZE//2)*(1-1/self.hp))
        else:
            pygame.draw.rect(surface, (150, 150, 150), (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)
    
    
    def add_score(self, player):
        if self.type == 'diamond':
            player.diamond += 1
        elif self.type == 'iron':
            player.iron += 1
        elif self.type == 'coal':
            player.coal += 1