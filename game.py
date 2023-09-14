import pygame

from settings import BG_COLOUR, RESOLUTION, RESOLUTION_MAIN, WIDTH, HEIGHT, FPS, CELL_SIZE, CELL_ROWS, CELL_COLUMS
from cell import Cell
from player import Player
from score import Score


pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
# screen_main = pygame.Surface(RESOLUTION_MAIN)
clock = pygame.time.Clock()
running: bool = True
game_map: list = []
player = Player()
score = Score()

def initiate():
    for column in range(CELL_COLUMS):
        game_map.append(Cell(column * CELL_SIZE, 0))
        for row in range(1, CELL_ROWS):
            game_map.append(Cell(column * CELL_SIZE, row * CELL_SIZE))

def events(run):
    pressed = pygame.key.get_pressed()
    
    # player movement
    if pressed[pygame.K_w] and player.y >= CELL_SIZE:
        player.y -= CELL_SIZE
    elif pressed[pygame.K_s] and player.y < HEIGHT-(CELL_SIZE*2.8):
        player.y += CELL_SIZE
    elif pressed[pygame.K_a] and player.x >= CELL_SIZE:
        player.x -= CELL_SIZE
    elif pressed[pygame.K_d] and player.x < WIDTH-(CELL_SIZE*1.8):
        player.x += CELL_SIZE
        

def update():
    player.update()
    for cell in game_map:
        if cell.position == player.position and not cell.discovered:
            if cell.type == 'diamond':
                player.diamond += 1
            elif cell.type == 'iron':
                player.iron += 1
            elif cell.type == 'coal':
                player.coal += 1
            cell.discovered = True


def draw():
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BG_COLOUR)
    
    # RENDER YOUR GAME HERE
    for cell in game_map:
        cell.draw(screen)
    player.draw(screen)
    
    # draw bottom score pallete
    score.draw(screen, player)
    
    # flip() the display to put your work on screen
    pygame.display.flip()


initiate()
while running:
    # poll for events
    # # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    events(run = running)
    update()
    draw()
    
    pygame.display.set_caption('MiningGame ' + str(clock.get_fps()))
    clock.tick(FPS)  # limits FPS to 60

pygame.quit()