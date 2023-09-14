import pygame

from settings import CELL_SIZE


types: dict ={
    'surface': {'colour': 'green',},
    'tunnel': {'colour': 'yellow',},
    'soil': {'colour': 'brown', 'rarity': 1},
    'coal': {'colour': 'black', 'rarity': 4},
    'iron': {'colour': 'silver', 'rarity': 6},
}

class Cell():
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.position: list = [x, y]
        if self.y == 0:
            self.type: str = 'surface'
            self.discovered: bool = True
        else:
            self.type: str = 'soil'
            self.discovered: bool = False
    
    
    def draw(self, surface):
        if self.type == 'surface':
            pygame.draw.rect(surface, 'green', (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)
        # else:
        if self.discovered:
            pygame.draw.rect(surface, 'yellow', (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)
        else:
            pygame.draw.rect(surface, 'gray', (self.x, self.y, CELL_SIZE, CELL_SIZE), 0)