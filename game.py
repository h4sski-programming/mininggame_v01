import pygame

from settings import BG_COLOUR, RESOLUTION, WIDTH, HEIGHT, FPS, CELL_SIZE, CELL_ROWS, CELL_COLUMS
from cell import Cell
from player import Player


pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
running: bool = True
game_map: list = []
player = Player()

def initiate():
    for column in range(CELL_COLUMS):
        game_map.append(Cell(column * CELL_SIZE, 0))
        game_map[-1].discovered = True
        for row in range(1, CELL_ROWS):
            game_map.append(Cell(column * CELL_SIZE, row * CELL_SIZE))

def events(run):
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         run = False
    
    pressed = pygame.key.get_pressed()
    
    # player movement
    if pressed[pygame.K_w] and player.y >= CELL_SIZE:
        player.y -= CELL_SIZE
    elif pressed[pygame.K_s] and player.y < HEIGHT-(2*CELL_SIZE):
        player.y += CELL_SIZE
    elif pressed[pygame.K_a] and player.x >= CELL_SIZE:
        player.x -= CELL_SIZE
    elif pressed[pygame.K_d] and player.x < WIDTH-(2*CELL_SIZE):
        player.x += CELL_SIZE
        

def update():
    player.update()
    for cell in game_map:
        # print(f'{cell.position = }, {player.position = }, {player.x = }, {player.y = }')
        if cell.position == player.position:
            # print(f'True! {cell.discovered = }')
            cell.discovered = True


def draw():
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BG_COLOUR)
    
    # RENDER YOUR GAME HERE
    # for row in range(CELL_ROWS):
    #     for column in range(CELL_COLUMS):
    #         pygame.draw.rect(screen, 'black', (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    for cell in game_map:
        cell.draw(screen)
    player.draw(screen)
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