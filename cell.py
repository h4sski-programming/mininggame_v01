import pygame
from random import random

from settings import CELL_SIZE, HEIGHT


types: dict ={
    'surface': {'colour': 'green',},
    'tunnel': {'colour': 'yellow',},
    'soil': {'colour': 'brown', 'rarity': 1, 'minimum_depth': 0},
    'coal': {'colour': 'black', 'rarity': 12, 'minimum_depth': 0.2},
    'iron': {'colour': 'purple', 'rarity': 30, 'minimum_depth': 0.4},
    'diamond': {'colour': 'lightblue', 'rarity': 50, 'minimum_depth': 0.7},
}

class Cell():
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.position: list = [x, y]
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
            elif rand <= 1 / types['iron']['rarity'] and y >= HEIGHT * types['iron']['minimum_depth']:
                self.type: str = 'iron'
                self.colour: str = types['iron']['colour']
            elif rand <= 1 / types['coal']['rarity'] and y >= HEIGHT * types['coal']['minimum_depth']:
                self.type: str = 'coal'
                self.colour: str = types['coal']['colour']
            else:
                self.type: str = 'soil'
                self.colour: str = types['soil']['colour']
    
    
    def draw(self, surface):
        if self.type == 'surface':
            pygame.draw.rect(surface, self.colour, (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)
        # else:
        if self.discovered:
            # pygame.draw.rect(surface, 'yellow', (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)
            pygame.draw.rect(surface, self.colour, (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)
        else:
            pygame.draw.rect(surface, 'gray', (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)