import pygame

from settings import CELL_SIZE, RESOLUTION, CELL_ROWS, SCORE_RECT, SCORE_FONT_SIZE

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', SCORE_FONT_SIZE)

class Score():
    def draw(self, surface, player):
        pygame.draw.rect(surface, 'black', SCORE_RECT, 0)
        text = my_font.render(f'COAL = {player.coal}, IRON = {player.iron}, DIAMOND = {player.diamond}', False, 'white')
        surface.blit(text, (SCORE_RECT[0] + 50, SCORE_RECT[1] + 10))