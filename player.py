import pygame

from settings import CELL_SIZE


class Player():
    def __init__(self) -> None:
        self.x: int = 0
        self.y: int = 0
        self.coal: int = 0
        self.iron: int = 0
        self.diamond: int = 0
    
    def update(self):
        self.position: list = [self.x, self.y]
    
    
    def draw(self, surface):
        pygame.draw.circle(surface, 'red', (self.x + CELL_SIZE/2, self.y + CELL_SIZE/2), (CELL_SIZE//2)*4//5)